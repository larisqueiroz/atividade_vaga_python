from rest_framework import serializers
from app.models import Arma, Municao

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'

class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = '__all__'