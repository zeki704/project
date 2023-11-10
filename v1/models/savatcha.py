from django.db import models
from maxsulot import Mahsulot
from auth import User


class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    miqdori = models.IntegerField(default=1)
    narxi = models.BigIntegerField(default=0)
    narx_type = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    status = models.BooleanField(default=True)

    def savat_format(self):
        return {
            "Mahsulot": self.mahsulot,
            "Miqdori": self.miqdori,
            "Narxi": self.narxi,
            "Narx_type": self.narx_type
        }

    def save(self, *args, **kwargs):
        self.narxi = int(self.mahsulot.mahsulot_sotish_narxi)*int(self.miqdori)
        self.narx_type = f"{self.mahsulot.mahsulot_sotish_narx_type}"

        return super(Savat, self).save(*args, **kwargs)

    def str(self):
        return f"{self.user}: {self.mahsulot}"