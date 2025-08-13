📚 Kütüphane Yönetim Sistemi
Bu proje, bir web arayüzü aracılığıyla kitapları yönetmenizi sağlayan basit ve modern bir kütüphane yönetim sistemidir. ISBN numarası ile hızlıca yeni kitaplar ekleyebilir, mevcut kitapları silebilir ve kütüphanenizdeki tüm kitapları listeleyebilirsiniz.

✨ Projenin Öne Çıkan Özellikleri:

Web Arayüzü: Kolay kullanımlı, kullanıcı dostu arayüz.

API Entegrasyonu: Kitap bilgilerini çekmek için Open Library API'sini kullanır.

Veri Kalıcılığı: Tüm kitap verileri library.json dosyasında güvenli bir şekilde saklanır.

Modern API: Güçlü ve esnek bir yapı için FastAPI ile geliştirildi.

🚀 Kurulum ve Başlatma
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki basit adımları takip edin.

Uvicorn: FastAPI sunucusunu çalıştırmak için.

Pydantic: Veri modelleri ve doğrulama için.

Httpx: Open Library API'sine istek göndermek için.

Open Library API: Kitap bilgilerini almak için kullanılan harici API.

1. git clone https://github.com/AydinBariss/KutuphaneProjesi.git
cd KutuphaneProjesi

2. Gerekli Kütüphaneleri Yükleyin
pip install -r requirements.txt

3. API Sunucusunu Başlatın
uvicorn api:app --reload

Sunucu başlatıldıktan sonra tarayıcınızda http://127.0.0.1:8000 adresine giderek projenin web arayüzüne erişebilirsiniz.

📖 Kullanım Kılavuzu
Web Arayüzü: index.html dosyasını tarayıcıda açarak uygulamayı kullanmaya başlayabilirsiniz.

API Belgeleri: Oluşturulan API'nin tüm uç noktalarını görmek ve test etmek için http://127.0.0.1:8000/docs adresini ziyaret edebilirsiniz.

📌 API Uç Noktaları:
Uç Nokta:
/books metot:GET Açıklama:Kütüphanedeki tüm kitapları listeler.
/add-by-isbn/{isbn} motot:POST Açıklama:Belirtilen ISBN'e sahip kitabı ekler.
/books/{isbn} metot:DELETE Açıklama:Belirtilen ISBN'e sahip kitabı siler.

