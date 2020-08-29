from rest_framework import serializers
from .models import Pet, History, Breed, Gender, Color, Size, Specie, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
        # depth = 1


class PetSerializer(serializers.ModelSerializer):
    # photos = PhotoSerializer(source='photos', many=True)
    history = serializers.SerializerMethodField()
    album = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ('__all__')

    def get_album(self, pet):
        photos = list(pet.photos.filter(deleted=False))
        data = PhotoSerializer(data=photos, context=self.context, many=True)
        if not data.is_valid():
            return data.data
        return {}

    def get_history(self, pet):
        return pet.history.filter(deleted=False).values()


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
