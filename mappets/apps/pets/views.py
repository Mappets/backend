from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import View


from rest_framework import status
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
    
    def retrieve(self, request, pk=None):
        queryset = Pet.objects.all()
        pet = get_object_or_404(queryset, pk=pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)
        

    def create(self, request, pk=None):
        try:
            data = request.data.copy()
            data.update({'user': request.user.id})
            serializer = PetSerializer(data=data)
            # import pdb ; pdb.set_trace()
            if serializer.is_valid():
                pet = serializer.save()
                data.update({'pet':pet.id})
            historySerializer = PetHistorySerializer(data=data)            
            if historySerializer.is_valid():
                history = historySerializer.save()
                return Response({
                    'message': 'Pet cadastrado com sucesso!',
                    'pet': pet.id,
                    'history': history.id
                    }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message':e}, status=status.HTTP_400_BAD_REQUEST)


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
