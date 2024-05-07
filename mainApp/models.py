from django.core.validators import MinValueValidator
from django.db import models

from userApp.models import Tarqatuvchi

class Mahsulot(models.Model):
    nom = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    narx1 = models.FloatField()
    narx2 = models.FloatField(blank=True, null=True)
    miqdor = models.FloatField()
    olchov = models.CharField(max_length=20)
    sana = models.DateField(auto_now=True)
    tarqatuvchi = models.ForeignKey(Tarqatuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
class Mijoz(models.Model):
    ism = models.CharField(max_length=100)
    dokon = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=14)
    manzil = models.TextField(max_length=255)
    qarz = models.FloatField(default=0, validators=[MinValueValidator(0)])
    oluvchi = models.CharField(max_length=20)
    tarqatuvchi = models.ForeignKey(Tarqatuvchi,on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'

