from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('perfil/<int:id>/', views.ver_perfil, name='ver_perfil'),
]