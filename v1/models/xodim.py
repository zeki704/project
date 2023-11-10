from django.db import models


class Xodim(models.Model):
    xodim_name = models.CharField(max_length=128)
    xodim_phone = models.CharField(max_length=128)
    xodim_passport_seriyasi = models.CharField(max_length=9)


    def xodim_format(self):
        return {
            "ID":self.id,
            "Xodim_name": self.xodim_name,
            "Xodim_Phone": self.xodim_phone,
            "Xodim_Passport_seriyasi": self.xodim_passport_seriyasi
        }

    def __str__(self):
        return self.xodim_name