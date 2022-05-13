from django.shortcuts import render
from app.api.serializers import ArmaSerializer, MunicaoSerializer
from app.models import Arma, Municao, Objeto, Objeto_Tipo, Calibre
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
import json

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

@api_view(['GET', 'POST'])
def ler_e_gravar_dados(request):
    if request.method == 'GET':
        arma_view = Arma.objects.all()
        municao_view = Municao.objects.all()
        arma_serialize = ArmaSerializer(arma_view, many=True)
        municao_serialize = MunicaoSerializer(municao_view, many=True)

        result = arma_serialize.data + municao_serialize.data
        return Response(result, status=status.HTTP_201_CREATED)
    

    if request.method == 'POST':
        print(type(request.data))
        content = json.loads(json.dumps(request.data))
        print(content)
        if "quantidade_de_tiros" in content or "imagem" in content:
            serializer = ArmaSerializer(data=request.data)
            tipo = 'arma'
            
        else:
            serializer = MunicaoSerializer(data=request.data)
            tipo = 'munição'

        calibre = Calibre.objects.get(desc_calibre=request.data['calibre']).id
        tipo_atual_id = Objeto_Tipo.objects.get(tipo_de_objeto=tipo).id
        objeto = Objeto.objects.create(objeto_tipo_id=tipo_atual_id)
        objeto.save()
        print(f'objeto tipo {tipo} salvo com a id referente a {tipo} que é {tipo_atual_id}')

        if tipo == 'arma':
            arma_obj = Arma.objects.create(id_obj_id=tipo_atual_id,marca=request.data['marca'],
            modelo=request.data['modelo'],quantidade_de_tiros=request.data['quantidade_de_tiros'],
            valor_estimado=request.data['valor_estimado'],imagem=request.data['imagem'],
            calibre_id_id=calibre)
            print(arma_obj)
            
            arma_obj.save()
            serializer = ArmaSerializer(data=arma_obj)
            print('salvou arma')
        else:
            municao = Municao.objects.create(id_obj_id=tipo_atual_id,marca=request.data['marca'],
            modelo=request.data['modelo'],
            valor_estimado=request.data['valor_estimado'],calibre_id_id=calibre)
            municao.save()

        if serializer.is_valid():
            serializer.save()

            print(serializer.data)
            return Response(dict(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

