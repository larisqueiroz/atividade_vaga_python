from django.contrib import admin
from .models import Arma, Municao, Objeto, Objeto_Tipo, Calibre
# Register your models here.

class ArmaAdmin(admin.ModelAdmin):
    list_display = ('calibre_id', 'marca', 'modelo', 
                                'quantidade_de_tiros', 'valor_estimado', 'imagem')
    list_filter = ('marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado')

class MunicaoAdmin(admin.ModelAdmin):
    list_display = ('calibre_id', 'marca', 'modelo', 
                                'valor_estimado')
    list_filter = ('marca', 'modelo', 'valor_estimado')

class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'objeto_tipo_id')

class CalibreAdmin(admin.ModelAdmin):
    list_display = ('id', 'desc_calibre')

class Objeto_TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_de_objeto')
                        

admin.site.register(Arma, ArmaAdmin)
admin.site.register(Municao, MunicaoAdmin)
admin.site.register(Objeto,ObjetoAdmin)
admin.site.register(Objeto_Tipo,Objeto_TipoAdmin)
admin.site.register(Calibre,CalibreAdmin)