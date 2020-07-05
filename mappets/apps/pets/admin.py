from django.contrib import admin
from .models import Pet, Breed, Gender, Specie, History


# Define o que vai ser manipulado no admin
admin.site.register(Pet)
admin.site.register(Breed)
admin.site.register(Gender)
admin.site.register(History)

