from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal
from app.infrastructure.repositories import UserRepository
from app.application.services import UserService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    try:
        return user_service.create_user(name, email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))