from django.contrib import admin
from .models import User


# Define o que irá ser manipulado pelo admin
admin.site.register(User)