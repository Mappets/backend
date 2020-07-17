from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse
from rest_framework import mixins,viewsets, generics as g
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



from .models import Pet, History, Breed, Gender, Color, Size, Specie

from .serializers import PetSerializer, PetHistorySerializer, PetBreedSerializer, PetGenderSerializer, PetColorSerializer, PetSizeSerializer, PetSpecieSerializer


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
        queryset = History.objects.all()
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


class PetBreedViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Breed GET List
    ---
    serializer: .serializers.PetBreedSerializer
    parameters:
        - name: string
        - description: 'Foobar long description goes here'
    """
    queryset = Breed.objects.all()
    serializer_class = PetBreedSerializer


class PetGenderViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Gender.objects.all()
    serializer_class = PetGenderSerializer




class PetColorViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Color.objects.all()
    serializer_class = PetColorSerializer
    permission_classes = [IsAuthenticated]


class PetSizeViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Size.objects.all()
    serializer_class = PetSizeSerializer


class PetSpecieViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Specie.objects.all()
    serializer_class = PetSpecieSerializer
