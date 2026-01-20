# TODO: Сделать custom-ые ошибки - закрыл
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException
from models import GetBooks, CreateBooks, PatchBooksBio, PutBooks
from custom_error_validation import register_handlers
import json

app = FastAPI()
register_handlers(app)

# TODO: Переписать на pydentic и вынести в отдельный файл (не забыть филды) - закрыл
# TODO: Нормально назвать поля (book_id)- закрыл

with open("books.json", "r", encoding='utf-8') as file:
    """Читает имеющие книги из файла books.json."""
    books = json.load(file)


def save_new_books() -> None:
    """Позволяет сохранить текущий список книг, а также новую книгу, которую пытаются добавить."""
    with open("books.json", "w", encoding="utf-8") as file_write:
        json.dump(books, file_write, ensure_ascii=False, indent=2)


@app.get(
    "/books",
    tags=["Книги"],
    summary="Получить все книги"
)
def read_book() -> list[dict[str, Any]]:
    return books


# TODO: Добавить Type-hint (аннотации)
@app.get(
    "/books/{book_id}",
    tags=["Книги"],
    summary="Получить конкретную книгу"
)
def read_book_by_id(book_id: int) ->GetBooks:
    for book in books:
        # if book.id == book_id:
        if book["book_id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Books not found")


@app.post("/books", tags=["Добавление"], summary=["Добавить книги"])
def create_book(new_book: str) -> CreateBooks:
    new_data = {
        "book_id": len(books) + 1,
        "author_name": new_book.author_name,
        "title": new_book.title,
        "bio": new_book.bio,
        "number": new_book.number,
        "email": new_book.Email
    }
    books.append(new_data)
    save_new_books()
    return new_data


@app.put("/books/{book_id}",
         tags=["Обновить полностью инофрмацию"],
          summary=["Обновить информацию по конкретной книге"]
         )
def books_update(book_id: int, book_in: PutBooks) -> PutBooks:
    for book in books:
        if book["book_id"] == book_id:
            book.update(book_in)
            save_new_books()
            return book
    raise HTTPException(status_code=404, detail="Books not found")

@app.patch("/books/{book_id}",
           tags=["Обнововить частично"],
           summary=["Обновить частично по конкретной книге"]
           )
def books_update(book_id: int, book_bio: PatchBooksBio) -> PatchBooksBio:
    for book in books:
        if book["book_id"] == book_id:
            partial_data = book_bio.model_dump(exclude_unset=True)
            book.update(partial_data)
            return GetBooks(**book)



# TODO: Возвращать созданую книгу - закрыл
# TODO: Добавить Git для версионирования
# TODO: Дописать все методы из CRUD
# TODO: С помощью библиотеки httpx вызывать каждый роут свой собственный

if __name__ == "__main__":
    uvicorn.run(app, port=8000)

# TODO:тесттест
