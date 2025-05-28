from django.urls import path
from .views import PublicarViajeView, ListarViajesView, TomarViajeView, EliminarViajeView

urlpatterns = [
    path('publicar/', PublicarViajeView.as_view(), name='publicar-viaje'),
    path('listar/', ListarViajesView.as_view(), name='listar-viajes'),
    path('tomar/', TomarViajeView.as_view(), name='tomar-viaje'),
    path('eliminar/<int:pk>/', EliminarViajeView.as_view(), name='eliminar-viaje'),
]