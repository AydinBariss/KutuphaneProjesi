import json
import httpx
from pydantic import BaseModel, Field
from typing import Optional, List

# Pydantic ile veri modelini tanımlıyoruz.
class Book(BaseModel):
    title: str
    author: str
    ISBN: str
    image_url: Optional[str] = Field(None)

class Library:
    def __init__(self, file_path='library.json'):
        self.file_path = file_path
        self.books: List[Book] = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            self.books = []

    def save_books(self):
        with open(self.file_path, 'w') as f:
            books_as_dict = [book.model_dump() for book in self.books]
            json.dump(books_as_dict, f, indent=4)

    def list_all_books(self):
        """Kütüphanedeki tüm kitapları listeler."""
        if not self.books:
            print("Kütüphanede henüz hiç kitap yok.")
        else:
            print("\nKütüphanedeki Kitaplar:")
            for book in self.books:
                print(f"- Başlık: {book.title}, Yazar: {book.author}, ISBN: {book.ISBN}")

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
            self.save_books()
            print(f"'{book.title}' kütüphaneye eklendi.")
        else:
            print("Hatalı giriş: Eklenecek öğe bir Book nesnesi olmalıdır.")

    def remove_book(self, isbn: str) -> bool:
        book_found = False
        for book in self.books:
            if book.ISBN == isbn:
                self.books.remove(book)
                self.save_books()
                print(f"ISBN: {isbn} numaralı kitap kütüphaneden silindi.")
                book_found = True
                break
        if not book_found:
            print(f"Hata: ISBN: {isbn} numaralı kitap kütüphanede bulunamadı.")
            return False
        return True

    def find_book(self, query: str) -> Optional[Book]:
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() == book.ISBN.lower():
                return book
        return None

    def get_book_details(self, isbn: str) -> Optional[Book]:
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
        try:
            with httpx.Client() as client:
                response = client.get(url, timeout=10.0)
                response.raise_for_status()

            data = response.json()
            if not data:
                return None

            book_data = data.get(f'ISBN:{isbn}')
            if not book_data:
                return None

            title = book_data.get('title', 'Başlık bulunamadı')
            authors = [author['name'] for author in book_data.get('authors', [])]
            author = ", ".join(authors) if authors else 'Yazar bulunamadı'
            image_url = book_data.get('cover', {}).get('medium', None)

            return Book(title=title, author=author, ISBN=isbn, image_url=image_url)
        except httpx.HTTPStatusError as e:
            print(f"Open Library API'den HTTP hatası geldi: {e}")
            return None
        except httpx.RequestError as e:
            print(f"Open Library API'ye istek gönderilirken bir hata oluştu: {e}")
            return None
        except Exception as e:
            print(f"Bilinmeyen bir hata oluştu: {e}")
            return None
