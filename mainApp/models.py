from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Bolim(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='bolimlar/')

    def __str__(self):
        return self.nom


class IchkiBolim(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='ichki-bolimlar/')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Mahsulotlar(models.Model):
    nom = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True, blank=True)
    ichki_bolim = models.ForeignKey(IchkiBolim, on_delete=models.CASCADE)
    batafsil = models.TextField(blank=True, null=True)
    narx = models.FloatField(validators=[MinValueValidator(0)])
    chegirma = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    baho = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    korish = models.PositiveSmallIntegerField(default=0)
    yetkazish = models.CharField(blank=True, null=True, max_length=255)
    buyurtma_soni = models.PositiveSmallIntegerField(default=0)
    kafolat = models.CharField(max_length=50, null=True, blank=True)
    mavjud = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Rasm(models.Model):
    mahsulotlar = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='mahsulotlar/')


    def __str__(self):
        return self.mahsulotlar.nom


class Xsusiyat(models.Model):
    mahsulotlar = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)
    qiymat = models.CharField(max_length=40)


    def __str__(self):
        return self.nom




