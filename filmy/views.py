from django.shortcuts import render
from django.http import HttpResponse
from .models import Film


# Create your views here.

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest test.</h1>")
    # test = "to jest coś we views"
    # return render(request, 'filmy/filmy.html', {'text': test})
    wszystkie = Film.objects.all()
    return render(request, 'filmy/filmy.html', {'filmy': wszystkie})



