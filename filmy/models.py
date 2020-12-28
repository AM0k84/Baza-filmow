from django.db import models


# Create your models here.
class DodatkoweInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat'),
    }
    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)


class Film(models.Model):
    tytul = models.CharField(max_length=80, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(blank=True, null=True)
    opis = models.TextField(default="")
    premiera = models.DateField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      blank=True, null=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)


class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Aktor(models.Model):
    imie = models.CharField(max_length=40)
    nazwisko = models.CharField(max_length=40)
    filmy = models.ManyToManyField(Film)


