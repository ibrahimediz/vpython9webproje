from django.db import models


class todolist(models.Model):
    konu = models.CharField(max_length=200)
    tanim = models.TextField()

    def __str__(self):
        return self.konu
    