from colorsys import rgb_to_hls
import email
from email.policy import default
from pyexpat import model
from django.db import models
from django import forms
from django.contrib.auth.models import User

from base.validators import validateCpf, validateEmail, validateEndereco, validateNome, validateRg, validateSenha


class Usuario(models.Model):
    
    CHOICES_USUARIO_DEPARTAMENTO = (
        ('1','Coodernação'),
        ('2', 'Professor'),
        ('3', 'Aluno')
    )

    CHOICES_USUARIO_TURNO = (
        ('1','Manhã'),
        ('2','Tarde'),
        ('3','Manhã e Tarde')
    )
    nome = models.CharField(
        max_length=100,
        blank=True,
		null=True,
		validators=[validateNome]
        )
    #foto = models.ImageField()
    email = models.CharField(
        max_length=100,
        null=True,
        unique=True,
		validators=[validateEmail]
        )

    cpf = models.CharField(
        max_length=11,
        blank=True,
		null=True,
		unique=True,
		validators=[validateCpf]
        )
    rg = models.CharField(
        max_length=7,
        blank=True,
		null=True,
		unique=True,
		validators=[validateRg]
        )
    endereco = models.CharField(
        max_length=100,
        blank=True,
		null=True,
		validators=[validateEndereco]
        )
    data_nascimento = models.DateField()
    data_entrada = models.DateField()
    turno = models.CharField(
        max_length=10,
        blank=True,
		null=True,
		choices=CHOICES_USUARIO_TURNO
        )
    departamento = models.CharField(
        default='',
        max_length=20,
        blank=True,
        null=True,
        choices=CHOICES_USUARIO_DEPARTAMENTO
        )   
    
    senha = models.CharField(
        max_length=8,
        blank=True,
		null=True,
		unique=True,
		validators=[validateSenha] )
    #historico = models.ImageField()
    #ativo = models.BooleanField()
    def __str__(self) -> str:
        return self.nome
