from pyexpat import model
from django.forms import fields
from django import forms
from .models import Usuario

class usuarioForm (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome',
                'email',
                'cpf',
                'rg',
                'endereco',
                'data_nascimento',
                'data_entrada',
                'turno',
                'departamento',
                'senha']

