from django.db import models

# Create your models here.

# coding: utf-8

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=15, blank=False, unique=True)
    nome_completo = models.CharField(max_length=100, blank=True )

    def __unicode__(self):
        return self.nome_usuario

class Historico(models.Model):
    usuario = models.ForeignKey(Usuario)
    data = models.DateTimeField('Data/hora')
    comando = models.CharField(max_length=10000)

    def __unicode__(self):
        return self.comando
