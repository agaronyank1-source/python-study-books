from sqlalchemy.orm import DeclarativeBase


"""Декларативный класс — это Python-класс,
 в котором ты в явном виде описываешь структуру таблицы (и связи) прямо в коде, 
 а ORM на основе этого описания строит “карту” соответствия"""

class Base (DeclarativeBase):
    pass
