from django.contrib import admin
from django.urls import path, include


'''
Define as rotas da aplicação
'''
urlpatterns = [
    path('', include('organizations.urls')),
    path('', include('pets.urls')),
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
