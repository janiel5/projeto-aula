from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    data_criacao = models.DateField()
    tipo_despesa = models.CharField(max_length=50)
    descricao  = models.CharField(max_length=250)
    forma_pagamento = {('boleto', 'boleto'),
                       ('credito','credito'),
                       ('debito', 'debito')
                       }
    def __str__(self):
        return str(self.data_criacao)

class Compra(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    unidadeCompra = models.CharField(max_length=30)
    qtdPrevistoMes = models.DecimalField(max_digits=7, decimal_places=2)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    precoMaximo = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome


# Create your models here.
