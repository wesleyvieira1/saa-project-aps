from tokenize import Name
from unicodedata import name
from urllib import request
from xml.dom.minidom import Document
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario
from usuario.forms import usuarioForm, usuarioSysForm
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from main import urls



#Listagem dos Usuários
class listagemUsuariosView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nome')

#Cadastro dos Usuários
class usuarioCreateView(SuccessMessageMixin,CreateView):
    model = Usuario
    form_class = usuarioForm
    success_url = '/home/'
    success_message = "Cadastrado com sucesso"

        
                
    def get_success_message(self, cleaned_data):
        return self.success_message 
#Editar Usuários

class usuarioUpdateView(UpdateView):
    model = Usuario
    form_class = usuarioForm
    success_url = '/usuarios/'

#Excluir Usuários

class usuarioDeleteView(DeleteView):
    model = Usuario
    success_url = '/usuarios/'


def register(request):
    if request.method=="POST":
        form = usuarioSysForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Login Registrado com Sucesso')
            return redirect('home')
        messages.error(request, 'Falha no registro do login')
    form = usuarioSysForm()
    context = {'form': form}
    return render(request, template_name='usuario/register.html', context=context)