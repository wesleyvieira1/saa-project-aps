from symbol import comp_if
from django.forms import ValidationError, fields, models
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser

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
    username = forms.ChoiceField(choices=[('0','--Selecione o CPF--')]+[(Usuario.cpf, Usuario.cpf) for Usuario in Usuario.objects.all()])
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    class Meta:
        model = User
        fields = ('username','password1','password2')
        help_texts = {k:"" for k in fields}


    def save(self, commit=True):
        user = super(usuarioSysForm, self).save(commit=False)

        if commit:
            user.save()
        return user