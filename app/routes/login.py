from fastapi import APIRouter, Depends, Request
from auth import get_current_user

login_router = APIRouter()

#login page
@login_router.get("/login")
def login_page(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "message.html",
        {
            "request": request,
            "name": "Login Page",
            "message": "You are already logged in.",
            "is_home": False,
        },
    )
    
#logout page
@login_router.get("/logout")
def logout_page(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "logout.html",
        {
            "request": request,
            "name": "Logout Page",
            "is_home": False,
        },
    )