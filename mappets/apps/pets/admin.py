from django.contrib import admin
from .models import Pet, Breed


# Define o que vai ser manipulado no admin
admin.site.register(Pet)
admin.site.register(Breed)

