from django.urls import path
from pdf.views import ConviteView

urlpatterns = [
    path('', ConviteView.as_view(), name='convite'),
]
