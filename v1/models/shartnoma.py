from django.db import models
from maxsulot import Mahsulot


class Shartnoma(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mahsulot_raqami = models.IntegerField(default=1)
    mahsulot_sanasi = models.DateTimeField()


class Shartnoma_kirganda(models.Model):
    shartnoma_id = models.ForeignKey(Shartnoma, on_delete=models.SET_NULL, null=True, blank=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True, blank=True)
    miqdori = models.PositiveIntegerField()
    total = models.IntegerField()
    sanasi = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total = self.mahsulot.mahsulot_sotish_narxi * self.miqdori
        return super(Shartnoma_kirganda, self).save(*args, **kwargs)
