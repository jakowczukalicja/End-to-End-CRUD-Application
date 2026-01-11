from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.user import user_router
from routes.home import home_router
from routes.login import login_router
from routes.likes import likes_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory="templates")
app.state.templates = templates

app.include_router(user_router)
app.include_router(home_router)
app.include_router(login_router)
app.include_router(likes_router)

