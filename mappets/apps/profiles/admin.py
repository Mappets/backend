from django.contrib import admin
from .models import Profile


# Define o que vai ser manipulado no admin
admin.site.register(Profile)

