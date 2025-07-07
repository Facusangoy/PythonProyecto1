from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path

from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("perfil", views.perfil, name="perfil"),
    path("edita-perfil", views.editarPerfil, name="editar_perfil"),     
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)