from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Yontem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Hizmet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}"
class Banka(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    iban = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}"
    
class Musteri(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = PhoneNumberField(blank=True)
    birthdate = models.DateField()
    address = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.uid}"
    
class Siparis(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    services = models.JSONField(default=list)
    date = models.DateTimeField()
    price = models.FloatField()
    debt = models.FloatField()
    
    def __str__(self):
        return f"{self.uid} - {self.date}"
    
    
class Odeme(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    date = models.DateTimeField()
    amount = models.FloatField()
    method = models.ForeignKey(Yontem, on_delete=models.SET_DEFAULT, default=0)
    note = models.TextField()
    
    def __str__(self):
        return f"{self.uid} - {self.date}"

class Randevu(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    services = models.JSONField(default=list)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
    note = models.TextField()
    
    def __str__(self):
        return f"{self.uid} - {self.date}"

class Settings(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    keywords = models.TextField()
    logo = models.ImageField()
    favicon = models.ImageField()

    def __str__(self):
        return f"{self.title}"