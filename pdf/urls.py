from django.urls import path
from pdf.views import Formulario

urlpatterns = [
    path('processar_formulario/', Formulario.as_view(), name='processar_formulario'),
]
