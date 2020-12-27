from django.db import models


# Create your models here.

class Film(models.Model):
    tytul = models.CharField(max_length=80, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.tytul} ({self.rok})"

