from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('__all__')

from rest_framework import serializers




class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "name", "email", "password")

class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        exclude = ('created_at','updated_at', 'deleted_at', 'deleted')