from django.shortcuts import render
from .models import Disciplina
from django.views.generic import CreateView
from .forms import disciplinaForm

class disciplinaCreateView(CreateView):
    model = Disciplina
    form_class = disciplinaForm
    success_url = '/home'
    success_message = "Cadastrado com sucesso"


    def get_success_message(self, cleaned_data):
        return self.success_message