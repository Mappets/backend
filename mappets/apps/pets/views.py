from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View


from rest_framework import status
from rest_framework import mixins, viewsets, generics as g
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser


from .models import Pet, History, Breed, Gender, Color, Size, Specie, Photo

from .serializers import (
    PetSerializer, PetHistorySerializer, PetBreedSerializer,
    PetGenderSerializer, PetColorSerializer, PetSizeSerializer,
    PetSpecieSerializer, PhotoSerializer
)


class PetViewSet(ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super(PetViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def create(self, request, pk=None):
        try:
            data = request.data.copy()
            data.update({'user': request.user.id})
            serializer = PetSerializer(data=data)
            if serializer.is_valid():
                pet = serializer.save()
                data.update({'pet': pet.id})
            historySerializer = PetHistorySerializer(data=data)
            if historySerializer.is_valid():
                history = historySerializer.save()
                return Response({
                    'message': 'Pet cadastrado com sucesso!',
                    'pet': pet.id,
                    'history': history.id
                }, status=status.HTTP_201_CREATED)
            return Response({
                'message': 'Erro ao cadastrar Pet!'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)


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


class PhotoUploadView(g.ListCreateAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        file_serializer = PhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
