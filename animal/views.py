from django.shortcuts import render
from rest_framework import viewsets
from .models import Animal, AnimalHistory
from .serializers import AnimalSerializer, AnimalHistorySerializer
from rest_framework.response import Response


class AnimalViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        try:
            req = request.data
            animal = Animal.objects.create(
                name=req['name'],
                age=req['age'],
                color=req['color'],
                gender=req['gender'],
                breed_id=req['breed'],
                species=req['species']
            )
            history = AnimalHistory.objects.create(
                animal=animal,
                address=req['address'],
                latitude=req['latitude'],
                longitude=req['longitude'],
                # TODO: user_id tem que ser o id do usuario logado. Implementar
                user_id=1
            )
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        except Exception as e:
            pass


class AnimalHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = AnimalHistory.objects.all()
        serializer = AnimalHistorySerializer(queryset, many=True)
        return Response(serializer.data)