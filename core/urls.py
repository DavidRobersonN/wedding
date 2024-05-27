from django.urls import path
from core.views import IndexView, check_guest

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('check_guest/', check_guest, name='check_guest'),
]
