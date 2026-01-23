from pydantic import BaseModel, EmailStr, Field


class BasePass(BaseModel): 1


pass


class BaseBooksModel(BaseModel):
    book_id: int = Field(title="ID книги")
    author_name: str = Field(title="Имя автора книги", max_length=30)
    title: str = Field(title="Название книги", max_length=70)
    bio: str | None = Field(title="БИО книги", default=None, max_length=200)
    number: int = Field(title="Номер телефона", ge=0, le=99999999999)
    email: EmailStr = Field(title="Почта автора")


class CreateBooks(BasePass):
    new_book: str = Field(title="Название новой книги")
    author_name: str = Field(title="Имя автора книги", max_length=30)
    title: str = Field(title="Название книги", max_length=70)
    bio: str | None = Field(title="БИО книги", default=None, max_length=200)
    number: int = Field(title="Номер телефона", ge=0, le=99999999999)
    Email: EmailStr = Field(title="Почта автора")


class GetBooks(BaseBooksModel):
    pass


class PatchBooksBio(BaseModel):
    title: str = Field(title="Название книги", max_length=70)
    number: int = Field(title="Номер телефона", ge=0, le=99999999999)


class PutBooks(BaseBooksModel):
    pass
