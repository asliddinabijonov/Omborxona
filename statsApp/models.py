from django.db import models

from mainApp.models import Mahsulot, Mijoz
from userApp.models import Tarqatuvchi


class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.FloatField()
    summa = models.FloatField()
    tolandi = models.FloatField(default=0)
    qarz = models.FloatField(default=0)
    sana = models.DateTimeField(auto_now_add=True)
    tarqatuvchi = models.ForeignKey(Tarqatuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mahsulot.nom} {self.mijoz.ism}"

    class Meta:
        verbose_name = 'Sotuv'
        verbose_name_plural = 'Sotuvlar'
