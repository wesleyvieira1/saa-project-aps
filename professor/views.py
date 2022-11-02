from django.shortcuts import render
from .models import Professor
from django.views.generic import CreateView
from .forms import professorForm

class professorCreateView(CreateView):
    model = Professor
    form_class = professorForm
    success_url = '/home'
    success_message = "Cadastrado com sucesso"


    def get_success_message(self, cleaned_data):
        return self.success_message