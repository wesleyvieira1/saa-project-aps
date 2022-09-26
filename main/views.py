from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from usuario.models import Usuario

class homeView(TemplateView):
    template_name = 'main/index.html'

