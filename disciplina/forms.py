from dataclasses import fields
from django import forms
from usuario.models import Usuario

from disciplina.models import Disciplina

class disciplinaForm (forms.ModelForm):
    ano = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Disciplina
        fields = ['nome_disciplina', 'nome_professor', 'ano']