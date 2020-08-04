from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response


from django.contrib.auth import get_user_model

from .serializers import UserSerializer, RegisterUserSerializer, ProfileSerializer



from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class RegisterUserView(generics.CreateAPIView):

    model = get_user_model()
    permission_classes = [ permissions.AllowAny,]
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        data_profile = {
            'name': request.data.get('name', None),
            'picture': request.data.get('picture', None),
            'phone': request.data.get('phone', None),
            'user': serializer.instance.pk
        }
        profile_serializer = ProfileSerializer(data=data_profile)
        profile_serializer.is_valid(raise_exception=True)
        self.perform_create(profile_serializer)
        
        res = {'message': _('Registration Successful')}
        res.update(dict(serializer.data.items()))
        res.update(dict(profile_serializer.data.items()))
        
        headers = self.get_success_headers(serializer.data)
        return Response(res, status=status.HTTP_201_CREATED, headers=headers)