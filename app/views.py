from django.shortcuts import render
from app.api.serializers import ArmaSerializer, MunicaoSerializer
from app.models import Arma, Municao
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

@api_view(['GET'])
def ver_dados_armazenados(request):
    arma_view = Arma.objects.all()
    municao_view = Municao.objects.all()
    arma_serialize = ArmaSerializer(arma_view, many=True)
    municao_serialize = MunicaoSerializer(municao_view, many=True)

    result = arma_serialize.data + municao_serialize.data
    return Response(result)