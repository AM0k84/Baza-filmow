from django.contrib import admin
from filmy.models import Film, DodatkoweInfo, Ocena


# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "rok", "imdb_rating"]
    list_filter = ("rok", "imdb_rating")
    search_fields = ("tytul", "opis",)

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)