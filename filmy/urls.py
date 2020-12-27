from django.urls import path
from filmy.views import wszystkie_filmy

urlpatterns = [
    path('wszystkie/', wszystkie_filmy)
    ]