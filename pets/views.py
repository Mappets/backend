from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response


from .models import Pet, History
from .serializers import PetSerializer, PetHistorySerializer

class IndexView(View):

    def get(self, request, *args, **kw):
        return HttpResponse(content='The Mappets API is working')


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


class PetHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = History.objects.all()
        serializer = PetHistorySerializer(queryset, many=True)
        return Response(serializer.data)