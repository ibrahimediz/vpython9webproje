from django.db import models
from django.utils import timezone

class IletisimModel(models.Model):
    Konu = models.CharField(max_length=200)
    Mesaj = models.TextField()
    ePosta = models.EmailField()
    Zaman = models.DateTimeField(default=timezone.now)
    resim = models.ImageField(null=True,upload_to='images/')

    def __str__(self):
        return self.Konu