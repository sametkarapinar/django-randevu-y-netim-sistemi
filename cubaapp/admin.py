from django.contrib import admin
from .models import Yontem, Musteri, Siparis, Odeme, Randevu, Hizmet, Banka

class YontemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['name']
    
class MusteriAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'uid', 'mail', 'phone', 'birthdate', 'address']
    search_fields = ['name', 'id', 'uid', 'mail', 'phone', 'birthdate', 'address']
    list_filter = ['name', 'id', 'uid', 'mail', 'phone', 'birthdate', 'address']
    
class SiparisAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'services', 'date', 'price', 'debt']
    search_fields = ['id', 'uid', 'services', 'date', 'price', 'debt']
    list_filter = ['id', 'uid', 'services', 'date', 'price', 'debt']
    
class OdemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'date', 'amount', 'method', 'note']
    search_fields = ['id', 'uid', 'date', 'amount', 'method', 'note']
    list_filter = ['id', 'uid', 'date', 'amount', 'method', 'note']
    

class RandevuAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'services', 'date', 'note']
    search_fields = ['id', 'uid', 'services', 'date', 'note']
    list_filter = ['id', 'uid', 'services', 'date', 'note']
    
class HizmetAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['name', 'description']
    
class BankaAdmin(admin.ModelAdmin):
    list_display = ['name', 'iban', 'owner', 'description']
    search_fields = ['name', 'iban', 'owner', 'description']
    list_filter = ['name', 'iban', 'owner', 'description']

    
admin.site.register(Yontem, YontemAdmin)
admin.site.register(Musteri, MusteriAdmin)
admin.site.register(Siparis, SiparisAdmin)
admin.site.register(Odeme, OdemeAdmin)
admin.site.register(Hizmet, HizmetAdmin)
admin.site.register(Randevu, RandevuAdmin)
admin.site.register(Banka, BankaAdmin)