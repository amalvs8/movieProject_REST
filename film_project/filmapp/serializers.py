from rest_framework import serializers
from . models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'name', 'description', 'director', 'cast']

