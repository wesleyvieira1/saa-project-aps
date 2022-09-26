from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario, UsuarioSys
from .forms import usuarioForm, usuarioForms

#Listagem dos Usuários
class listagemUsuariosView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nome')

#Cadastro dos Usuários
class usuarioCreateView(CreateView):
    model = Usuario
    form_class = usuarioForm
    success_url = '/usuarios/'

#Editar Usuários
class usuarioUpdateView(UpdateView):
    model = Usuario
    form_class = usuarioForm
    success_url = '/usuarios/'

#Excluir Usuários

class usuarioDeleteView(DeleteView):
    model = Usuario
    success_url = '/usuarios/'

