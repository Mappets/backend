from django.shortcuts import render
from rest_framework import viewsets
from .models import Organization
from .serializers import OrganizationSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer