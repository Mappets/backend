from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    full_name = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    class Meta:
        model = UserModel
        fields = (
                'id',
                'name',
                'email',
                'phone',
                'organizations',
                'is_staff',
                'is_superuser',
                'is_active',
                'date_joined',
                'full_name',
                'profile',
                'first_name',
                'last_name',
                'created_at',
                'updated_at'
                )


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
        fields = ( "id", "name", "email", "password",)

