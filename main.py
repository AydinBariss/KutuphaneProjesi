from library import Library, Book

def main():
    library = Library() # Library sınıfının bir örneğini oluştur
    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Ekle")
        print("2. Tüm Kitapları Listele")
        print("3. Kitap Ara")
        print("4. Kitap Sil")
        print("5. Çıkış")

        choice = input("Lütfen bir seçenek girin: ")

        if choice == "1":
            # Kitap ekleme işlemleri
            isbn = input("Eklenecek kitabın ISBN numarasını girin: ")

            # API'den kitap bilgilerini çekiyoruz
            new_book = library.get_book_details(isbn)
            
            if new_book:
                library.add_book(new_book)
            else:
                print("Hata: Girilen ISBN numarasına ait kitap bulunamadı.")
        elif choice == "2":
            # Tüm kitapları listeleme işlemi
            library.list_all_books()
        elif choice == "3":
            # Kitap arama işlemleri
            query = input("Başlık, yazar veya ISBN ile arama yapın: ")
            found_books = library.find_book(query)
            if found_books:
                print("\nArama Sonuçları:")
                for book in found_books:
                    print(book)
            else:
                print("Eşleşen kitap bulunamadı.")
        elif choice == "4":
            # Kitap silme işlemleri
            isbn = input("Silinecek kitabın ISBN numarasını girin: ")
            library.remove_book(isbn)
        elif choice == "5":
            print("Kütüphane sisteminden çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()