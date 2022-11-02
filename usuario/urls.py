from unicodedata import name
from django.urls import path
from .views import listagemProfessorView,listagemUsuariosView, register, usuarioCreateView, usuarioUpdateView, usuarioDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(listagemUsuariosView.as_view()), name='usuario.index'),
    path('professorLista/', login_required(listagemProfessorView.as_view()), name='professor.index'),
    path('novo/',login_required(usuarioCreateView.as_view()), name='usuario.novo'),
    path('editar/<int:pk>',login_required(usuarioUpdateView.as_view()), name='usuario.editar'),
    path('excluir/<int:pk>',login_required(usuarioDeleteView.as_view()), name='usuario.excluir'),
    path('novo/register', login_required(register), name='usuario.register'),
]