from django.contrib import admin
from .models import Category, Organization


# Define o que vai ser manipulado no admin
admin.site.register(Category)
admin.site.register(Organization)