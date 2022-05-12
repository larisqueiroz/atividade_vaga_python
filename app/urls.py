from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_dados_armazenados, name='ver_dados_armazenados'),
    path('delete/<str:pk>', views.delete, name='delete')
]