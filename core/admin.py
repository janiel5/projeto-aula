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
