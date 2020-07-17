from rest_framework import serializers
from .models import Pet, History, Breed, Gender, Color, Size, Specie


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


class PetGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('__all__')


class PetColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('__all__')


class PetSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('__all__')


class PetSpecieSerializer(serializers.ModelSerializer):
    breeds = PetBreedSerializer(many=True, read_only=True)
    class Meta:
        model = Specie
        fields = ('__all__')
