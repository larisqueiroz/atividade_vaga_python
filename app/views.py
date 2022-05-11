from django.shortcuts import render
from app.api.serializers import ArmaSerializer, MunicaoSerializer
from app.models import Arma, Municao, Objeto, Objeto_Tipo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

@api_view(['GET', 'POST'])
def ver_dados_armazenados(request):
    if request.method == 'GET':
        arma_view = Arma.objects.all()
        municao_view = Municao.objects.all()
        arma_serialize = ArmaSerializer(arma_view, many=True)
        municao_serialize = MunicaoSerializer(municao_view, many=True)

        result = arma_serialize.data + municao_serialize.data
        return Response(result, status=status.HTTP_201_CREATED)
    

    if request.method == 'POST':
        if request.data['quantidade_de_tiros'] or request.data['imagem']:
            serializer = ArmaSerializer(data=request.data)
            tipo = 'arma'
            id_tipo = Objeto_Tipo.objects.filter(tipo_de_objeto=tipo).get()
        else:
            serializer = MunicaoSerializer(data=request.data)
            tipo = 'municao'
            id_tipo = Objeto_Tipo.objects.filter(tipo_de_objeto=tipo).get()

        print(serializer)
        print(tipo)
        objeto = Objeto.objects.create(objeto_tipo_id=id_tipo,id=request.data['id'])
        objeto.save()
        
        if serializer.is_valid():
            
            # id_obj = Objeto_Tipo.objects.create(tipo_de_objeto=objeto_tipo)
            # request.data['id_obj'] = objeto['objeto_tipo_id']
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
