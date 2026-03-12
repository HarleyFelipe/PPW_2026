from django.urls import path
from .views import Index, Sobre, Contato, Modelo

urlpatterns = [
    path("", Index.as_view(), name="pagina_inicial"),
    path("sobre/", Sobre.as_view(), name="sobre"),
    path("contato/", Contato.as_view(), name="contato"),
    path("modelo/", Modelo.as_view(), name="modelo"),
]
