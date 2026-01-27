from http.client import responses

import httpx

BASE_URL = "http://127.0.0.1:8000"


def test_get_all_books():
    response = httpx.get(f"{BASE_URL}/books")
    print("GET/books", response.status_code, response.json())


def test_get_book_by_id():
    book_id = input("Введите ID книги: ")
    response = httpx.get(f"{BASE_URL}/books/{book_id}")
    print(f"GET/books/{book_id}",
          response.status_code, response.json())


def test_post_book():
   new_book = input("Write book name: ")
   new_test_book = {
       "new_book": new_book,
       "author_name": "HTTPX_test",
       "title": "HTTPX_test",
       "bio": "HTTPX_test",
       "number": 8444757558,
       "email": "user@example.com"
   }
   response = httpx.post(f"{BASE_URL}/books", json=new_test_book)
   print("POST/books", response.status_code, response.json())

def test_put_book():
    full_data = {
        "author_name": "HTTPX_test",
        "title": "HTTPX_test",
        "bio": "HTTPX_test",
        "number": 8444757558,
        "email": "user@example.com"
    }
    response = httpx.put(f"{BASE_URL}/books/1", json=full_data)
    print("PUT/books", response.status_code, response.json())

def test_patch_book():
    partial_data = {
        "title": "HTTPX_test",
        "number": 100000348
                    }
    response = httpx.patch(f"{BASE_URL}/books/1", json=partial_data)
    print("PATCH/books", response.status_code, response.json())


if __name__ == "__main__":
    test_get_all_books(),
    test_get_book_by_id(),
    test_post_book(),
    test_put_book(),
    test_patch_book()
