from symbol import comp_if
from django.forms import fields, models
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class usuarioForm (forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    data_entrada = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    #foto = forms.FileField()
    #historico = forms.FileField()
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


class usuarioSysForm(UserCreationForm):
    #email = forms.EmailField(required=True);
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(usuarioSysForm, self).save(commit=False)
        #user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
       