from rest_framework import serializers
from .models import Pet, History, Breed, Gender, Color, Size, Specie, Photo


class PetSerializer(serializers.ModelSerializer):
    # color = serializers.SerializerMethodField()
    # gender = serializers.SerializerMethodField()
    # size = serializers.SerializerMethodField()
    # specie = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ('__all__')
    
    # def create(self, validated_data):
    #     import pdb ; pdb.set_trace()
    #     print('teste')

    # def get_color(self, pet):
    #     print(pet.id)
    #     return pet.color.name
    
    # def get_gender(self, pet):
    #     return pet.gender.name
    
    # def get_size(self, pet):
    #     return pet.size.name
    
    # def get_specie(self, pet):
    #     return pet.specie.name
    def get_history(self, pet):
        return pet.history.all().values()

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

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
