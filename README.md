Kütüphane Yönetim Sistemi
Bu proje, bir web arayüzü ile yönetilebilen basit bir kütüphane yönetim sistemidir. Kullanıcılar, ISBN numarası girerek kütüphaneye yeni kitaplar ekleyebilir, mevcut kitapları silebilir ve listeyi görüntüleyebilir.

Proje, üç ana bileşenden oluşmaktadır:

FastAPI API: Backend işlemlerini yönetir.

Python Sınıfları: Kitap ve kütüphane verilerinin mantığını içerir.

Web Arayüzü: Kullanıcıların projeyle etkileşime girmesini sağlar.

Kullanılan Teknolojiler
Python 3.10+

FastAPI: Web API'sini oluşturmak için.

Uvicorn: FastAPI sunucusunu çalıştırmak için.

Pydantic: Veri modelleri ve doğrulama için.

Httpx: Open Library API'sine istek göndermek için.

Open Library API: Kitap bilgilerini almak için kullanılan harici API.

Kurulum ve Çalıştırma
Projenin yerel olarak çalıştırılması için aşağıdaki adımları izleyin.

Projeyi Klonlama:

git clone https://github.com/KullaniciAdin/KutuphaneProjesi.git
cd KutuphaneProjesi

Gerekli Kütüphaneleri Yükleme:

pip install -r requirements.txt

API Sunucusunu Başlatma:

uvicorn api:app --reload

Sunucu başlatıldıktan sonra http://127.0.0.1:8000 adresine erişebilirsiniz.

Kullanım Kılavuzu
Web Arayüzü: Tarayıcınızda index.html dosyasını açarak uygulamayı kullanabilirsiniz.

API Belgeleri: API'nin tüm uç noktalarını görmek ve test etmek için http://127.0.0.1:8000/docs adresini ziyaret edebilirsiniz.

API Uç Noktaları
GET /books: Kütüphanedeki tüm kitapları listeler.

POST /add-by-isbn/{isbn}: Belirtilen ISBN'e sahip kitabı kütüphaneye ekler.

DELETE /books/{isbn}: Belirtilen ISBN'e sahip kitabı siler.