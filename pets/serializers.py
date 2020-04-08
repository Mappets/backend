from rest_framework import serializers
from .models import Pet, History, Breed


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('__all__')


class PetHistorySerializer(serializers.ModelSerializer):
    Pet = PetSerializer(many=False, read_only=True)

    class Meta:
        model = History
        fields = ('__all__')


class PetBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('__all__')
