from django.urls import path
from .views import homeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/', login_required(homeView.as_view()), name='home')
]