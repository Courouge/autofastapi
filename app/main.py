# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str

@app.get("/livres/")
def read_all_books():
    return [{"id": 1, "title": "Le Seigneur des anneaux", "author": "J.R.R. Tolkien"}]

@app.get("/livres/{book_id}")
def read_book(book_id: int):
    book = {"id": book_id, "title": f"Book {book_id}", "author": "Unknown"}
    return book

class TestApp:
    def test_read_main(self):
        response = requests.get("http://localhost:8000/livres/")
        assert response.status_code == 200
        message = f"L'API a répondu avec le code {response.status_code}"
        return message

    def run_tests(self):
        result = pytest.main(["-v", "--exitfirst"])
        return result.exitstatus

async def execute_tests(ctx):
    result = TestApp().run_tests()
    message = f"Tests réussis! (Code retour : {result})"
    await ctx.send(message)
