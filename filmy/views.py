from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import FilmForm
from .models import Film


# Create your views here.

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest test.</h1>")
    # test = "to jest coś we views"
    # return render(request, 'filmy/filmy.html', {'text': test})
    wszystkie = Film.objects.all()
    return render(request, 'filmy/filmy.html', {'filmy': wszystkie})


def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'filmy/film_form.html', {'form': form})


def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'filmy/film_form.html', {'form': form})


def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'filmy/potwierdz.html', {'film': film})
