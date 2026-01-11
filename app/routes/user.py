from fastapi import APIRouter, Depends, Request, Form
from auth import get_current_user
from database import engine
from sqlalchemy import text
from fastapi.responses import RedirectResponse

user_router = APIRouter()

#read info about current user
@user_router.get("/me")
def me(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    
    user_id = current_user["user_id"]
    user_name = current_user["name"]
    user_surname = current_user["surname"]
    user_email = current_user["email"]
   
    return templates.TemplateResponse(
        "user_info.html",
        {
            "request": request,
            "name": "User Info",
            "user_id": f"{user_id}",
            "user_name": f"{user_name}",
            "user_surname": f"{user_surname}",
            "user_email": f"{user_email}",
            "is_home": False,
        },
    )

#read info about all users
@user_router.get("/users")
def get_all_users(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    
    with engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM count_user_likes"))
        dict_res = res.mappings().all()
        return templates.TemplateResponse(
        "page_with_table.html",
        {
            "request": request,
            "name": "Users",
            "is_home": False,
            "dict_res": dict_res
        },
        )
  
#create new users      
@user_router.get("/create_user")
def create_user_page(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "create_user.html",
        {"request": request,
         "name": "Create user",
         "is_home": False},
    )

@user_router.post("/create_user")
def create_user(
    request: Request,
    name: str = Form(...),
    surname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    templates = request.app.state.templates
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO users (name, surname, email, password)
                    VALUES (:name, :surname, :email, :password)
                """),
                {"name": name, "surname": surname, "email": email, "password": password},
            )
    except IntegrityError:
       
        return templates.TemplateResponse(
            "create_user.html",
            {"request": request,
            "name": "Create user",
            "is_home": False,
            "error": "Email already exists. Please use a different email."},
            status_code=400,
        )


    return RedirectResponse(url="/login", status_code=303)

#update password
@user_router.get("/change_password")
def change_password_page(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "change_password.html",
        {"request": request,
         "name": "Change Password",
         "is_home": False},
    )


@user_router.post("/change_password")
def change_password(
    password: str = Form(...),
    current_user: dict = Depends(get_current_user),
):
    templates = request.app.state.templates
    with engine.begin() as conn:
        conn.execute(
            text(
                """
                UPDATE users SET password = :password
                WHERE user_id = :user_id
                """
            ),
            {"user_id": current_user["user_id"], "password": password},
        )
    return RedirectResponse(url="/", status_code=303)

#delete user
@user_router.get("/delete_user")
def change_password_page(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "delete_user.html",
        {"request": request,
         "name": "Delete User",
         "is_home": False},
    )


@user_router.post("/delete_user")
def delete_user(current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    with engine.begin() as conn:
        conn.execute(
            text(
                """
                DELETE FROM users WHERE user_id = :user_id
                """
            ),
            {"user_id": current_user["user_id"]},
        )
    return RedirectResponse(url="/", status_code=303)