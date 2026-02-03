from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from .base import Base


class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String(30), nullable=False)
    number = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False, unique=True)

"""Можно NULL (если nullable=True)
Нельзя чтобы был NULL - (nullable=False)"""

books = relationship("Book", back_populates="author")
