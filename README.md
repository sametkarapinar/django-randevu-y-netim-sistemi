# Django Randevu Yönetim Sistemi

Bu sistem, müşterilerin randevularını, ödemelerini ve hizmetlerini takip etmek amacıyla hazırlanmıştır.

## Özellikler

- Müşteri Ekleme ve Çıkarma
- Hizmet Ekleme ve Çıkarma
- Banka Bilgisi Ekleme ve Çıkarma
- Müşteri Listeleme ve Görüntüleme
- Randevu Ekleme, Onaylama ve Silme
- Randevu Onaylama ile Sipariş Oluşturma
- Hizmet Fiyatlarını Siparişe Çekme
- Fiyat ve Borç Bilgileri Girme
- Ödeme Girince Kalan Borçtan Düşme

## Kurulum

Gerekli bağımlılıkları yükleyin:

```pip install -r requirements.txt```

Veritabanı migrasyonlarını çalıştırın:

```python manage.py migrate```

Geliştirme sunucusunu başlatın:

```python manage.py runserver```


# Kullanım

1) Müşteri İşlemleri
* Müşteri Ekleme
* Yeni bir müşteri eklemek için gerekli bilgileri girin ve kaydedin.

2) Müşteri Çıkarma
* Listeden müşteriyi seçip silme işlemi gerçekleştirin.

3) Müşteri Listeleme
* Sistemde kayıtlı olan tüm müşterileri listeleyin.

4) Müşteri Görüntüleme
* Seçilen müşterinin detay bilgilerini görüntüleyin.

5) Hizmet İşlemleri
* Hizmet Ekleme
* Yeni bir hizmet eklemek için gerekli bilgileri girin ve kaydedin.

6) Hizmet Çıkarma
* Listeden hizmeti seçip silme işlemi gerçekleştirin.

7) Banka Bilgisi İşlemleri
* Banka Bilgisi Ekleme
* Yeni bir banka bilgisi eklemek için gerekli bilgileri girin ve kaydedin.

8) Banka Bilgisi Çıkarma
* Listeden banka bilgisini seçip silme işlemi gerçekleştirin.

9) Randevu İşlemleri
* Randevu Ekleme
* Yeni bir randevu eklemek için gerekli bilgileri girin ve kaydedin.

10) Randevu Onaylama
* Randevuyu onaylayarak sipariş oluşturun ve hizmet fiyatlarını çekin.

11) Randevu Silme
* Listeden randevuyu seçip silme işlemi gerçekleştirin.

12) Sipariş ve Ödeme İşlemleri
* Sipariş Oluşturma
* Onaylanan randevulardan sipariş oluşturun ve hizmet fiyatlarını çekin.

13) Fiyat ve Borç Bilgileri Girme
* Siparişe ait fiyat ve borç bilgilerini girin.

14) Ödeme Girme
* Ödeme bilgilerini girerek kalan borçtan düşülmesini sağlayın.

# Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir çekme isteği gönderin veya bir sorun bildirimi yapın.


`Sistem geliştirme aşamasındadır.`
