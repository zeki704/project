from django.db import models
from mijoz import Mijoz


class savdo_oynasi(models.Model):
    mahsulot_nomi = models.CharField(max_length=150)
    mahsulot_rangi = models.CharField(max_length=150)
    razmer = models.CharField(max_length=128)
    soni = models.IntegerField(default=0)
    mijoz_bolsa = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True, blank=True)
    sotish_narxi = models.CharField(max_length=128)
    valyutasi = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS"),
    ])
    def __str__(self):
        return self.mahsulot_nomi