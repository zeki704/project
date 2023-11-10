from django.db import models


class Mijoz(models.Model):
    mijoz_name = models.CharField(max_length=150)
    mijoz_phone = models.CharField(max_length=50)
    mijoz_haridlar_oraligi = models.DateTimeField(auto_now=True)
    xabar_berish = models.DateTimeField(auto_now=True)

    def mijoz_format(self):
        return {
            "ID": self.id,
            "Mijoz_name": self.mijoz_name,
            "Mijoz_phone": self.mijoz_phone,
            "Mijoz_haridlar_oraligi": self.mijoz_haridlar_oraligi,
            "Xabar_berish": self.xabar_berish
        }
    def __str__(self):
        return self.mijoz_name