from django.urls import path
from . import views

urlpatterns = [
    path('', views.ler_e_gravar_dados, name='ver_dados_armazenados'),
]