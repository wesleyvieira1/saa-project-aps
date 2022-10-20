from colorsys import rgb_to_hls
from distutils.command.upload import upload
import email
from email.policy import default
from pyexpat import model
from django.db import models
from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.forms import PasswordInput
from django.core.validators import RegexValidator

from base.validators import validateContato, validateCpf, validateDigits, validateEmail, validateEndereco, validateFoto, validateHistorico, validateNoDigits, validateNome, validateRg, validateSenha

def usuario_file_name(instance, filename):
    return '/'.join(['usuario', instance.user.username, filename])

class Usuario(models.Model):
    
    CHOICES_USUARIO_DEPARTAMENTO = (
        ('1','Coodernação'),
        ('2', 'Professor'),
        ('3', 'Aluno')
    )

    CHOICES_USUARIO_TURNO = (
        ('1','Manhã'),
        ('2','Tarde'),
        ('3','Integral')
    )
    nome = models.CharField(
        max_length=100,
        blank=False,
		null=True,
		validators=[validateNome,validateNoDigits]
        )
    #foto = models.ImageField()
    email = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        unique=True,
		validators=[validateEmail]
        )
    contato = models.CharField(
        max_length=11,
        null=True,
        blank=False,
        validators=[validateContato])

    cpf = models.CharField(
        max_length=11,
        blank=False,
		null=True,
		unique=True,
		validators=[validateCpf]
        )
    rg = models.CharField(
        max_length=7,
        blank=False,
		null=True,
		unique=True,
		validators=[validateRg]
        )
    endereco = models.CharField(
        max_length=100,
        blank=False,
		null=True,
		validators=[validateEndereco]
        )
    data_nascimento = models.DateField()
    data_entrada = models.DateField()
    foto = models.ImageField(
        blank=True, 
        upload_to=usuario_file_name, 
        validators=[validateFoto])
    historico = models.FileField(
        blank=True, 
        upload_to=usuario_file_name, 
        validators=[validateHistorico])
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
    #historico = models.ImageField()
    #ativo = models.BooleanField()
    def __str__(self) -> str:
        return self.nome

