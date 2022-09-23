from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login

class homeView(TemplateView):
    template_name = 'main/index.html'

