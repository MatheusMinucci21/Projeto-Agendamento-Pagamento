from django.contrib import admin
from django.urls import path, include

#URL do Projeto para que possamos postar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('agendamentos.urls')),
]