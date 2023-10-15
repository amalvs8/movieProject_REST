import json
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Film
from .serializers import FilmSerializer
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET', 'POST'])
def film_list(request, format=None):
    # to give GET response
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
    # to give POST response
    if request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([serializer.data], status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def film_detail(request, id, format=None):
    # fetch data from DB matching primary key
    try:
        film = Film.objects.get(pk=id)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response([serializer.data])
    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([serializer.data])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        film.delete()
        return Response({'message': 'Content deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


def get_detail(request):
    response = requests.get('http://127.0.0.1:8000/films/')
    data = response.json()
    print(data)
    return render(request, 'demo.html', {'data': data})


def get_film(request, id):
    response = requests.get('http://127.0.0.1:8000/films/{}'.format(str(id)))
    data = response.json()
    return render(request, 'film.html', {'data': data})


def post_data(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            director = request.POST['director']
            cast = request.POST['cast']
    except:
        pass
    data = {
        'name': name,
        'description': description,
        'director': director,
        'cast': cast
    }
    data = json.dumps(data)
    url = 'http://127.0.0.1:8000/films/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    data = response.json()
    print(data)
    return render(request, 'film.html', {'data': data})
