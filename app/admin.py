from django.contrib import admin
from .models import Arma, Municao, Objeto, Objeto_Tipo, Calibre
# Register your models here.

class ArmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'calibre_id', 'marca', 'modelo', 
                                'quantidade_de_tiros', 'valor_estimado', 'imagem')
    list_filter = ('marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado')

class MunicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'calibre_id', 'marca', 'modelo', 
                                'valor_estimado')
    list_filter = ('marca', 'modelo', 'valor_estimado')

admin.site.register(Arma, ArmaAdmin)
admin.site.register(Municao, MunicaoAdmin)
admin.site.register(Objeto)
admin.site.register(Objeto_Tipo)
admin.site.register(Calibre)