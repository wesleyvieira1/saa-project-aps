from django.urls import path
from .views import professorCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('novo/', login_required(professorCreateView.as_view()), name='professor.novo')
]