from unicodedata import name
from django.urls import path
from .views import listagemUsuariosView, usuarioCreateView, usuarioUpdateView

urlpatterns = [
    path('',listagemUsuariosView.as_view(), name='usuario.index'),
    path('novo/',usuarioCreateView.as_view(), name='usuario.novo'),
    path('editar/<int:pk>',usuarioUpdateView.as_view(), name='usuario.editar')
]