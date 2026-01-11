from fastapi import APIRouter, Depends, Request, HTTPException
from auth import get_current_user
from database import engine
from sqlalchemy import text
import json

likes_router = APIRouter()
COLOR_CONFIG = {
    "beige": "rgb(204, 174, 135)",
    "black": "rgb(0,0,0)",  
    "blue": "rgb(117, 199, 224)",
    "brown": "rgb(145, 105, 73)",
    "green": "rgb(127, 240, 113)",
    "pink": "rgb(255, 156, 233)",
    "grey": "rgb(143, 142, 136)",
    "orange": "rgb(235, 155, 84)",
    "red": "rgb(227, 67, 59)",
    "white": "rgb(255, 255, 255)",
    "yellow": "rgb(255, 249, 158)"

   
}

def get_color_rgb(color_name: str) -> str:
    return COLOR_CONFIG.get(color_name.lower(), color_name)

@likes_router.get("/garments")
def get_all_garments(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    
    with engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM info_about_garments"))
        dict_res = res.mappings().all()
        
        colours_res = conn.execute(text("SELECT DISTINCT colour FROM info_about_garments ORDER BY colour"))
        available_colours = [row[0] for row in colours_res]
        
        return templates.TemplateResponse(
        "garments.html",
        {
            "request": request,
            "name": "All Garments",
            "is_home": False,
            "dict_res": dict_res,
            "available_colours": available_colours,
            "selected_colour": None,
            "get_color_rgb": get_color_rgb
        },
        )
        


@likes_router.get("/garments/by-colour")
def get_garments_by_colour(request: Request, colour: str, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    
    with engine.connect() as conn:
        res = conn.execute(
            text("SELECT * FROM info_about_garments WHERE colour = :colour"),
            {"colour": colour},
        )
        dict_res = res.mappings().all()

        colours_res = conn.execute(text("SELECT DISTINCT colour FROM info_about_garments ORDER BY colour"))
        available_colours = [row[0] for row in colours_res]
        
        return templates.TemplateResponse(
            "garments.html",
            {
                "request": request,
                "name": f"Garments - {colour}",
                "is_home": False,
                "dict_res": dict_res,
                "available_colours": available_colours,
                "selected_colour": colour,
                "get_color_rgb": get_color_rgb
            },
        )


@likes_router.get("/garments/liked")
def get_liked_garments(request: Request, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    user_id = current_user["user_id"]

    with engine.connect() as conn:
        res = conn.execute(
            text(
                """
                SELECT g.*
                FROM info_about_garments g
                JOIN garment_like l ON l.garment_id = g.garment_id
                WHERE l.user_id = :user_id
                ORDER BY g.garment_id
                """
            ),
            {"user_id": user_id},
        )
        dict_res = res.mappings().all()
        colours_res = conn.execute(text("SELECT DISTINCT colour FROM info_about_garments ORDER BY colour"))
        available_colours = [row[0] for row in colours_res]

        return templates.TemplateResponse(
            "garments.html",
            {
                "request": request,
                "name": "My Liked Garments",
                "is_home": False,
                "dict_res": dict_res,
                "available_colours": available_colours,
                "selected_colour": None,
                "get_color_rgb": get_color_rgb,
                "is_liked_page": True,
            },
        )


@likes_router.get("/garments/liked/by-colour")
def get_liked_garments_by_colour(request: Request, colour: str, current_user: dict = Depends(get_current_user)):
    templates = request.app.state.templates
    user_id = current_user["user_id"]

    with engine.connect() as conn:
        res = conn.execute(
            text(
                """
                SELECT g.*
                FROM info_about_garments g
                JOIN garment_like l ON l.garment_id = g.garment_id
                WHERE l.user_id = :user_id AND g.colour = :colour
                ORDER BY g.garment_id
                """
            ),
            {"user_id": user_id, "colour": colour},
        )
        dict_res = res.mappings().all()
        colours_res = conn.execute(text("SELECT DISTINCT colour FROM info_about_garments ORDER BY colour"))
        available_colours = [row[0] for row in colours_res]

        return templates.TemplateResponse(
            "garments.html",
            {
                "request": request,
                "name": f"My Liked Garments - {colour}",
                "is_home": False,
                "dict_res": dict_res,
                "available_colours": available_colours,
                "selected_colour": colour,
                "get_color_rgb": get_color_rgb,
                "is_liked_page": True,
            },
        )


@likes_router.post("/garments/{garment_id}/like")
def like_garment(garment_id: int, current_user: dict = Depends(get_current_user)):
    user_id = current_user["user_id"]
    with engine.connect() as conn:
        existing = conn.execute(
            text("SELECT * FROM garment_like WHERE user_id = :user_id AND garment_id = :garment_id"),
            {"user_id": user_id, "garment_id": garment_id}
        ).one_or_none()
        
        if existing:
            return {"liked": True, "message": "Already liked"}
        conn.execute(
            text("INSERT INTO garment_like (user_id, garment_id) VALUES (:user_id, :garment_id)"),
            {"user_id": user_id, "garment_id": garment_id}
        )
        conn.commit()
        return {"liked": True, "message": "Liked"}


@likes_router.post("/garments/{garment_id}/unlike")
def unlike_garment(garment_id: int, current_user: dict = Depends(get_current_user)):
    user_id = current_user["user_id"]
    with engine.connect() as conn:
        conn.execute(
            text("DELETE FROM garment_like WHERE user_id = :user_id AND garment_id = :garment_id"),
            {"user_id": user_id, "garment_id": garment_id}
        )
        conn.commit()
        return {"liked": False, "message": "Unliked"}


@likes_router.get("/garments/{garment_id}/is-liked")
def is_garment_liked(garment_id: int, current_user: dict = Depends(get_current_user)):
    user_id = current_user["user_id"]
    with engine.connect() as conn:
        query = text("SELECT * FROM garment_like WHERE user_id = :user_id AND garment_id = :garment_id")
        params = {"user_id": user_id, "garment_id": garment_id}
        result = conn.execute(query, params).one_or_none()
        return {"liked": result is not None}