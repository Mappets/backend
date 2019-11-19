from django.contrib import admin
from .models import Organization


# Define o que vai ser manipulado no admin
admin.site.register(Organization)