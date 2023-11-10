from django.db import models

class Mahsulot(models.Model):
    mahsulot_nomi = models.CharField(max_length=150)
    mahsulot_olchami = models.CharField(max_length=150)
    mahsulot_rangi = models.CharField(max_length=150)
    mahsulot_location = models.CharField(max_length=150)
    mahsulot_soni = models.IntegerField()
    mahsulot_sotish_narxi = models.IntegerField(default=0)
    mahsulot_sotish_narxi_type = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    maxsulot_kirib_kelgan_narxi = models.IntegerField(default=0)
    mahsulot_kirib_kelgan_narxi_type = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])

    def mahsulot_format(self):
        return {
            "ID": self.id,
            "Mahsulot_nomi": self.mahsulot_nomi,
            "Mahsulot_o'lchami": self.mahsulot_olchami,
            "Mahsulot_rangi": self.mahsulot_rangi,
            "Mahsulot_Location": self.mahsulot_location,
            "Mahsulot_soni": self.mahsulot_soni,
            "Mahsulot_sotish_narxi": self.mahsulot_sotish_narxi,
            "Mahsulot_kirib_kelgan_narxi": self.maxsulot_kirib_kelgan_narxi
        }
    def __str__(self):
        return self.mahsulot_nomi