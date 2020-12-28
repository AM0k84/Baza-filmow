from django.contrib.auth.models import User
from rest_framework import serializers

from filmy.models import Film


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['tytul', 'rok', 'opis']
