from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, TIMESTAMP, JSON, Boolean, ForeignKey
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Integer, ForeignKey, TIMESTAMP
from datetime import datetime

from database import Base

class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    premissions: Mapped[str] = mapped_column(JSON, nullable=False)

class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Role.id), default=1)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, default=datetime.utcnow)
