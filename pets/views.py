from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .models import Pet, History, Breed
from .serializers import PetSerializer, PetHistorySerializer, PetBreedSerializer


class PetViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Pet.objects.all()
        serializer = PetSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        try:
            req = request.data
            pet = Pet.objects.create(
                name=req['name'],
                age=req['age'],
                color=req['color'],
                gender=req['gender'],
                breed_id=req['breed'],
                species=req['species']
            )
            history = History.objects.create(
                pet=pet,
                address=req['address'],
                latitude=req['latitude'],
                longitude=req['longitude'],
                # TODO: user_id tem que ser o id do usuario logado. Implementar
                user_id=1
            )
            serializer = PetSerializer(pet)
            return Response(serializer.data)
        except Exception as e:
            pass


class PetHistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = PetHistorySerializer

    def list(self, request):
        queryset = History.objects.first()
        serializer = PetHistorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        pass

    def delete(self, request):
        pass
    
    def update(self, request):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

class PetBreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = PetBreedSerializer