from dataclasses import fields
from django import forms
from usuario.models import Usuario

from professor.models import Professor

class professorForm (forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome_professor']