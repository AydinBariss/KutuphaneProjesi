from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from library import Library, Book
from typing import List

# FastAPI uygulamasını başlat
app = FastAPI()

# CORS'i etkinleştiriyoruz
# Bu, web tarayıcınızdan gelen isteklerin API'ye erişmesine izin verir.
# Geliştirme aşamasında her şeye izin vermek için ["*"] kullanıyoruz.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Kütüphane nesnesini global olarak başlat
library = Library()

@app.get("/")
def read_root():
    """Kütüphane API'sinin ana sayfası."""
    return {"message": "Kütüphane API'sine hoş geldiniz!"}

# Tüm kitapları listeleme endpoint'i
@app.get("/books", response_model=List[Book])
def get_all_books():
    """Tüm kitapları listeleyen endpoint."""
    return library.books

# Yeni kitap ekleme endpoint'i (sadece ISBN ile)
@app.post("/add-by-isbn/{isbn}", response_model=Book)
def add_book_with_isbn(isbn: str):
    """Belirtilen ISBN'e sahip kitabı API'den çekip ekleyen endpoint."""
    book_details = library.get_book_details(isbn)
    if not book_details:
        raise HTTPException(status_code=404, detail=f"ISBN: {isbn} numaralı kitap bulunamadı.")
    
    library.add_book(book_details)
    return book_details

# ISBN'e göre kitap silme endpoint'i
@app.delete("/books/{isbn}")
def remove_existing_book(isbn: str):
    """Belirtilen ISBN'e sahip kitabı silen endpoint."""
    if library.remove_book(isbn):
        return {"message": "Kitap başarıyla silündi."}
    else:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")



# API dokümantasyonu için
# Tarayıcıda http://127.0.0.1:8000/docs adresini ziyaret edin.