from symbol import comp_if
from django.forms import fields, models
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class usuarioForm (forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    data_entrada = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Usuario
        fields = ['nome',
                'email',
                'contato',
                'cpf',
                'rg',
                'endereco',
                'data_nascimento',
                'data_entrada',
                'turno',
                'departamento',
                'foto',
                'historico']


class usuarioSysForm(UserCreationForm):
    email = forms.EmailField(required=True);
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        help_texts = {k:"" for k in fields}

    def save(self, commit=True):
        user = super(usuarioSysForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
       