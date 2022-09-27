from django.contrib import admin
from django.urls import path, include

from main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('usuarios/', include('usuario.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
