from rest_framework import serializers
from .models import Animal, AnimalHistory


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('__all__')


class AnimalHistorySerializer(serializers.ModelSerializer):
    Animal = AnimalSerializer(many=False, read_only=True)

    class Meta:
        model = AnimalHistory
        fields = ('__all__')
