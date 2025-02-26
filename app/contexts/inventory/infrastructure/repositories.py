from sqlalchemy.orm import Session
from app.domain.user import User
from app.infrastructure.database import Base, engine, SessionLocal
from sqlalchemy import Column, String

class UserModel(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, user: User):
        db_user = UserModel(id=user.id, name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def find_by_email(self, email: str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()