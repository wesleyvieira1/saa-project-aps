from colorsys import rgb_to_hls
import email
from pyexpat import model
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=256)
    #foto = models.ImageField()
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=7)
    endereco = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_entrada = models.DateField()
    turno = models.CharField(max_length=10)
    #departamento = models.CharField(max_length=20)
    senha = models.CharField(max_length=8)
    #historico = models.ImageField()
    #ativo = models.BooleanField()
    def __str__(self) -> str:
        return self.nome
