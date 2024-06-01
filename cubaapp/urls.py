from django.urls import path
from . import views


urlpatterns = [
    path('anasayfa', views.indexPage,name='index'),

    path('musteriler', views.musteriler,name='musteriler'),
    path('musteriler/goruntule/<int:id>', views.musteri_goruntule,name='musteri_goruntule'),
    
    path('hizmetler', views.hizmetler,name='hizmetler'),
    path('hizmetler/stats', views.hizmet_istatistik,name='hizmet_istatistik'),

    path('banka/liste', views.banka_hesaplari,name='banka_hesaplari'),

    path('site/ayarlar', views.site_ayarlar,name='site_ayarlar'),


#AJAX İşlemleri

    path('ajax/musteri/ekle', views.ajax_musteri_ekle,name='ajax_musteri_ekle'),
    path('ajax/musteri/sil', views.ajax_musteri_sil,name='ajax_musteri_sil'),
    path('ajax/musteri/guncelle', views.ajax_musteri_guncelle,name='ajax_musteri_guncelle'),

    path('ajax/randevu/ekle', views.ajax_randevu_ekle,name='ajax_randevu_ekle'),
    path('ajax/randevu/onayla', views.ajax_randevu_onayla,name='ajax_randevu_onayla'),

    path('ajax/siparis/ekle', views.ajax_siparis_ekle,name='ajax_siparis_ekle'),
    path('ajax/siparis/sil', views.ajax_siparis_sil,name='ajax_siparis_sil'),

    path('ajax/odeme/ekle', views.ajax_odeme_ekle,name='ajax_odeme_ekle'),

    path('ajax/hizmet/ekle', views.ajax_hizmet_ekle,name='ajax_hizmet_ekle'),
    path('ajax/hizmet/sil', views.ajax_hizmet_sil,name='ajax_hizmet_sil'),
    path('ajax/hizmet/guncelle', views.ajax_hizmet_guncelle,name='ajax_hizmet_guncelle'),

    path('ajax/banka/ekle', views.ajax_banka_ekle,name='ajax_banka_ekle'),
    path('ajax/banka/guncelle', views.ajax_banka_duzenle,name='ajax_banka_duzenle'),
    
    #path('ajax/site/bilgiguncelle', views.update_site_settings,name='update_site_settings'),

]