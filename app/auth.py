from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import text
from database import engine

security = HTTPBasic()

def authenticate_user(email: str, password: str) -> dict | None:
    with engine.connect() as conn:
        row = conn.execute( 
            text(
                """
                SELECT user_id, name, surname, email
                FROM users
                WHERE email = :email AND password = :password
                """
            ),
            {"email": email, "password": password},
        ).mappings().one_or_none()
        return dict(row) if row else None


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> dict:
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user