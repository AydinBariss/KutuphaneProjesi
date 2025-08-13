import os
import json
import pytest
from library import Library, Book

# Her testten önce çalışacak fixture'ı tanımlayalım
@pytest.fixture
def empty_library():
    # Test için boş bir library.json dosyası oluştur
    file_path = "test_library.json"
    if os.path.exists(file_path):
        os.remove(file_path)
    return Library(file_path=file_path)

def test_add_book(empty_library):
    # Yeni bir kitap nesnesi oluştur
    book_to_add = Book(title="Ulysses", author="James Joyce", ISBN="978-0199535675")
    
    # Kitabı ekle
    empty_library.add_book(book_to_add)
    
    # 1. Kontrol: Liste uzunluğu 1 olmalı
    assert len(empty_library.books) == 1
    
    # 2. Kontrol: Eklenen kitap listede doğru şekilde yer almalı
    assert empty_library.books[0] == book_to_add
    
    # 3. Kontrol: Dosyaya doğru şekilde kaydedilmiş mi?
    with open(empty_library.file_path, "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["title"] == "Ulysses"



# Test için içinde kitap olan bir fixture tanımlayalım
@pytest.fixture
def populated_library(empty_library):
    book_to_add = Book(title="Ulysses", author="James Joyce", ISBN="978-0199535675")
    empty_library.add_book(book_to_add)
    # add_book'un print çıktısını testlerden gizlemek için
    # testin kendisi print yapmadığı sürece gözükmez
    return empty_library

def test_remove_book_success(populated_library):
    # Bir kitabı sil
    isbn_to_remove = "978-0199535675"
    populated_library.remove_book(isbn_to_remove)

    # 1. Kontrol: Liste uzunluğu 0 olmalı
    assert len(populated_library.books) == 0

    # 2. Kontrol: Silinen kitabın listede olmadığından emin ol
    assert not any(book.ISBN == isbn_to_remove for book in populated_library.books)
    
    # 3. Kontrol: Dosyadan da silinmiş mi?
    with open(populated_library.file_path, "r") as f:
        data = json.load(f)
    assert len(data) == 0

def test_remove_book_not_found(populated_library):
    # Var olmayan bir ISBN ile silme işlemi yap
    isbn_to_remove = "999-9999999999"
    initial_book_count = len(populated_library.books)

    populated_library.remove_book(isbn_to_remove)

    # Kitap bulunamadığı için liste uzunluğu değişmemeli
    assert len(populated_library.books) == initial_book_count
    
    # Dosya içeriği de değişmemeli
    with open(populated_library.file_path, "r") as f:
        data = json.load(f)
    assert len(data) == initial_book_count