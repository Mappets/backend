from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializers import UserSerializer, RegisterUserSerializer



from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class RegisterUserView(generics.CreateAPIView):

    model = get_user_model()
    permission_classes = [ permissions.AllowAny,]
    serializer_class = RegisterUserSerializer