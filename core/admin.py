from django.contrib import admin

from .models import *

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome','email','telefone')

admin.site.register(Contato, ContatoAdmin)

class DespesaAdmin(admin.ModelAdmin):
    list_display =  ('data_criacao', 'tipo_despesa', 'descricao', 'forma_pagamento')


admin.site.register(Despesa, DespesaAdmin)

class CompraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'unidadeCompra', 'qtdPrevistoMes', 'preco',
                    'precoMaximo')

admin.site.register(Compra, CompraAdmin)


# Register your models here.
class APartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero','qtdQuartos','proprietario','valorCondominio')

admin.site.register(Apartamento, APartamentoAdmin)

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('cliente','texto_Cliente','texto_Anuncio','preco','telefone','secao','tipo_Anuncio')

admin.site.register(Anuncio, AnuncioAdmin)