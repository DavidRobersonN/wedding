from django.urls import path
from core.views import IndexView, Formulario

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('processar_formulario/', Formulario.as_view(), name='processar_formulario'),
]
