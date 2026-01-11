from fastapi import APIRouter, Request

home_router = APIRouter()

#home page
@home_router.get("/")
def home(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(
        "message.html",
        {
            "request": request,
            "name": "Home",
            "message": "Welcome to our web app!",
            "is_home": True,
        },
    )
