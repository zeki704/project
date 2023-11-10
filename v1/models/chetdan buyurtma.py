from django.db import models
from maxsulot import Mahsulot

class Buyurtma_chetdan(models.Model):
    shartnoma_raqami = models.IntegerField()
    davlat_nomi = models.CharField(max_length=128)
    zavod_nomi = models.CharField(max_length=128)
    sanasi = models.DateTimeField()
    xolati = models.CharField(max_length=128, choices=[
        ("Tuzildi", "Tuzildi"),
        ("Yakunlandi", "Yakunlandi"),
        ("Yo'lda", "Yo'lda"),
        ("Qabul qilindi", "Qabul qilindi"),
    ])
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True, blank=True)

    def chetdan_buyurtma_mahsulot(self):
        return {
            "ID": self.id,
            "Shartnoma_raqami": self.shartnoma_raqami,
            "Davlat_nomi": self.davlat_nomi,
            "Zavod_nomi": self.zavod_nomi,
            "Sanasi": self.sanasi,
            "Xolati": self.xolati
        }
    def __str__(self):
        return self.shartnoma_raqami