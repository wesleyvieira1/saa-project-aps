from django.urls import path
from .views import disciplinaCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('nova/', login_required(disciplinaCreateView.as_view()), name='disciplina.novo')
]