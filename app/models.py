from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Calibre(models.Model):
    desc_calibre = models.CharField(max_length=45)

    def __str__(self):
        return self.desc_calibre

class Objeto_Tipo(models.Model): # TODO: verificar o tipo do id!!!!!!
    tipo_de_objeto = models.CharField(max_length=64)

    def __str__(self):
        return self.tipo_de_objeto

class Objeto(models.Model):
    objeto_tipo_id = models.ForeignKey(Objeto_Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.objeto_tipo_id

class Arma(models.Model):
    arma = models.OneToOneField(Objeto,on_delete=models.CASCADE,primary_key=True)
    calibre = models.ForeignKey(Calibre, on_delete=models.CASCADE)
    # calibre = models.CharField(max_length=64, blank=True) # R=TODO tirar esse blank
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField()
    valor_estimado = models.DecimalField(decimal_places=2,max_digits=10)
    imagem = models.CharField(max_length=128)

    def __str__(self):
        return self.modelo

class Municao(models.Model):
    id = models.OneToOneField(Objeto,on_delete=models.CASCADE,primary_key=True)
    calibre_id = models.ForeignKey(Calibre, on_delete=models.CASCADE)
    # calibre = models.CharField(max_length=64)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.modelo


