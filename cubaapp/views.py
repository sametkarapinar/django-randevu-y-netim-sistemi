from django.shortcuts import render
from .models import Musteri, Siparis, Odeme, Randevu, Hizmet, Yontem, Banka #Settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
import logging
import uuid
import datetime
logger = logging.getLogger(__name__)



def indexPage(request):
   context={"breadcrumb":{"parent":"Yönetim","child":"Anasayfa"}}
   return render(request,'general/index.html',context)







# Müşteriler Kategorisi

def musteriler(request):
   
   musteriler = Musteri.objects.all()
   
   context={"breadcrumb":{"parent":"Müşteri Yönetimi","child":"Müşteriler"},"musteriler":musteriler}
   return render(request,'musteri/musteriler.html',context)

def musteri_goruntule(request, id):
    musteri = Musteri.objects.get(id=id)
    uid = musteri.uid
    
    siparis = Siparis.objects.filter(uid=uid)
    odeme = Odeme.objects.filter(uid=uid)
    
    sonrandevular = Randevu.objects.filter(uid=uid, status=True).order_by('-date')[:3]
    
    randevular = Randevu.objects.filter(uid=uid)
    
    hizmetler = Hizmet.objects.all()
    
    context = {
        "breadcrumb": {"parent": "Müşteri Yönetimi", "child": "Müşteri Görüntüle"},
        "musteri": musteri,
        "siparis": siparis,
        "odeme": odeme,
        "sonrandevular": sonrandevular,
        "randevular": randevular,
        "hizmetler": hizmetler
    }
    
    return render(request, 'musteri/islemler/goruntule.html', context)
 
 
 
 
def hizmetler(request):
    hizmetler = Hizmet.objects.all()
    
    context = {
        "breadcrumb": {"parent": "Hizmet Yönetimi", "child": "Hizmetler"},
        "hizmetler": hizmetler
    }
    
    return render(request, 'hizmet/hizmetler.html', context)
 
 
def site_ayarlar(request):
    context = {
        "breadcrumb": {"parent": "Site Yönetimi", "child": "Site Ayarları"}
    }
    
    return render(request, 'site/ayarlar.html', context)
 
 
def hizmet_istatistik(request):
    hizmetler = Hizmet.objects.all()
    
    context = {
        "breadcrumb": {"parent": "Hizmet Yönetimi", "child": "Hizmetler"},
        "hizmetler": hizmetler
    }
    
    return render(request, 'hizmet/hizmetler.html', context)
 
 
 
def banka_hesaplari(request):
    bankalar = Banka.objects.all()
    
    context = {
        "breadcrumb": {"parent": "Banka Yönetimi", "child": "Banka Hesaapları"},
        "bankalar": bankalar
    }
    
    return render(request, 'banka/hesaplar.html', context)



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
@csrf_protect
def ajax_siparis_ekle(request):
    if request.method == 'POST':
        musteri = request.POST.get('musteri')
        date = request.POST.get('date')
        debt = request.POST.get('debt')
        services = request.POST.getlist('service[]')
        
        if not musteri or not date or not debt or not services:
            return JsonResponse({"status": "error"})
        
        hizmet_query = Hizmet.objects.filter(id__in=services)
        
        hizmetler = [
            {"id": h.id, "name": h.name} for h in hizmet_query
        ]
        
        siparis = Siparis.objects.create(
            uid=musteri,
            date=date,
            price=0,
            debt=debt,
            services=hizmetler 
        )
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})
     
     
@csrf_protect
def ajax_odeme_ekle(request):
    if request.method == 'POST':
        musteri = request.POST.get('musteri')
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        method_id = request.POST.get('method')
        siparis = request.POST.get('siparis')

        logger.debug("Method name received: %s", method_id)

        if not musteri or not date or not amount or not method_id:
            return JsonResponse({"status": "error", "message": "Missing required fields"})

        try:
            yontem = Yontem.objects.get(id=method_id)
        except Yontem.DoesNotExist:
            logger.error("Yontem with name %s does not exist", method_id)
            return JsonResponse({"status": "error", "message": "Invalid payment method"})

        try:
            siparis_instance = Siparis.objects.get(pk=siparis)
            siparis_instance.debt -= float(amount)
            siparis_instance.save()
            odeme = Odeme.objects.create(
                uid=musteri,
                date=date,
                amount=amount,
                method=yontem,
                note=siparis + " ID'li sipariş ödemesi yapıldı."
            )
            return JsonResponse({"status": "success"})
        except Exception as e:
            logger.error("Error creating Odeme instance: %s", str(e))
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed"})
    
    
def ajax_randevu_ekle(request):
    if request.method == 'POST':
        musteri = request.POST.get('musteri')
        date = request.POST.get('date')
        note = request.POST.get('note')
        services = request.POST.getlist('service[]')
        
        if not musteri or not date or not services:
            return JsonResponse({"status": "error", "message": "Missing required fields"})
        
        hizmet_query = Hizmet.objects.filter(id__in=services)
        
        hizmetler = [
            {"id": h.id, "name": h.name} for h in hizmet_query
        ]
        
        randevu = Randevu.objects.create(
            uid=musteri,
            date=date,
            note=note,
            services=hizmetler
        )
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed"})
    

def ajax_musteri_ekle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        dogumtarihi = request.POST.get('dogumtarihi')
        adres = request.POST.get('adres')
        
        if not name or not phone or not mail or not dogumtarihi or not adres:
            return JsonResponse({"status": "error", "message": "Tüm alanları doldurun."})
        
        uid = uuid.uuid4()
        
        try:
            musteri = Musteri.objects.create(
                uid=uid,
                name=name,
                mail=mail,
                phone=phone,
                birthdate=dogumtarihi, 
                address=adres  
            )
            
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    
def ajax_musteri_sil(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        
        if not id:
            return JsonResponse({"status": "error", "message": "Müşteri ID'si eksik."})
        
        try:
            musteri = Musteri.objects.get(id=id)
            musteri.delete()
            return JsonResponse({"status": "success"})
        except Musteri.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Müşteri bulunamadı."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    
@csrf_protect
def ajax_musteri_guncelle(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        adress = request.POST.get('adress')
        dogumtarihi = request.POST.get('dogumtarihi')
        
        
        if not uid or not name or not phone or not email or not adress or not dogumtarihi:
            return JsonResponse({"status": "error", "message": "Tüm alanları doldurun."})
        
        if " " in phone:
            phone = phone.replace(" ", "")
            
        if not phone.startswith("+"):
            return JsonResponse({"status": "error", "message": "Telefon numarası ülke kodu ile başlamalıdır."})

        try:
            musteri = Musteri.objects.get(uid=uid)
            musteri.name = name
            musteri.phone = phone
            musteri.mail = email
            musteri.address = adress
            musteri.birthdate = dogumtarihi
            musteri.save()
            return JsonResponse({"status": "success"})
        
        except Musteri.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Müşteri bulunamadı."})
        
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    
    
def ajax_siparis_sil(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        
        if not id:
            return JsonResponse({"status": "error", "message": "Sipariş ID'si eksik."})
        
        try:
            siparis = Siparis.objects.get(id=id)
            siparis.delete()
            return JsonResponse({"status": "success"})
        except Siparis.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Sipariş bulunamadı."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    
    
    
def ajax_randevu_onayla(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if not id:
            return JsonResponse({"status": "error", "message": "Randevu ID'si eksik."})
        
        try:
            randevu = Randevu.objects.get(id=id)

            fiyat = 0
            for hizmet in randevu.services:
                hizmet_query = Hizmet.objects.get(id=hizmet['id'])
                fiyat += hizmet_query.price

            randevu.status = True
            randevu.save()
            
            siparis = Siparis.objects.create(
                uid=randevu.uid,
                date=randevu.date,
                price=fiyat,
                debt=fiyat,
                services=randevu.services
            )
            return JsonResponse({"status": "success"})
        except Randevu.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Randevu bulunamadı."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    

@csrf_protect
def ajax_hizmet_ekle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        if not name or not price:
            return JsonResponse({"status": "error", "message": "Tüm alanları doldurun."})
        
        try:
            hizmet = Hizmet.objects.create(
                name=name,
                description=description,
                price=price
            )
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    


@csrf_protect
def ajax_hizmet_guncelle(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        if not id or not name or not price:
            return JsonResponse({"status": "error", "message": "Tüm alanları doldurun."})
        
        try:
            hizmet = Hizmet.objects.get(id=id)
            hizmet.name = name
            hizmet.description = description
            hizmet.price = price
            hizmet.save()
            return JsonResponse({"status": "success"})
        except Hizmet.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Hizmet bulunamadı."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    

@csrf_protect
def ajax_hizmet_sil(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        
        if not id:
            return JsonResponse({"status": "error", "message": "Hizmet ID'si eksik."})
        
        try:
            hizmet = Hizmet.objects.get(id=id)
            hizmet.delete()
            return JsonResponse({"status": "success"})
        except Hizmet.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Hizmet bulunamadı."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    
def ajax_banka_ekle(request):
    if request.method == 'POST':

        name = request.POST.get('bankName')
        owner = request.POST.get('bankOwner')
        description = request.POST.get('bankDescription')
        iban = request.POST.get('bankIBAN')

        if not name or not owner or not description or not iban:
            return JsonResponse({"status": "error", "message": "Tüm alanları doldurun."})
        
        try:
            banka = Banka.objects.create(
                name=name,
                iban=iban,
                description=description
            )
            return JsonResponse({"status": "success"})
        
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    

def ajax_banka_duzenle(request):
    if request.method == 'POST':
        id = request.POST.get('bankId')
        name = request.POST.get('bankName')
        owner = request.POST.get('bankOwner')
        description = request.POST.get('bankDescription')
        iban = request.POST.get('bankIBAN')
        
        if not id or not name or not owner or not description or not iban:
            return JsonResponse({"status": "error", "message": "Tüm alanları doldurun."})
        
        try:
            banka = Banka.objects.get(id=id)
            banka.name = name
            banka.owner = owner
            banka.description = description
            banka.iban = iban
            banka.save()
            return JsonResponse({"status": "success"})
        except Banka.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Banka bulunamadı."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})



#def update_site_settings(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        keywords = request.POST.get('keywords')
        logo = request.POST.get('logo')
        favicon = request.POST.get('favicon')
        
        if not title or not description or not keywords or not logo or not favicon:
            return JsonResponse({"status": "error", "message": "Tüm alanları doldurun."})
        
        try:
            site_settings = Settings.objects.get(id=1)
            site_settings.title = title
            site_settings.description = description
            site_settings.keywords = keywords
            site_settings.logo = logo
            site_settings.favicon = favicon
            site_settings.save()
            return JsonResponse({"status": "success"})
        except Settings.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Site ayarları bulunamadı."})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})