from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from .base import Base


class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    author_name = Column(String(30), nullable=False)
    title = Column(String(70), nullable=False)
    bio = Column(String(300), nullable=False)

    author = relationship("Author", back_populates="books")
