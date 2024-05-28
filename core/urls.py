from django.urls import path
from core.views import IndexView, CheckGuestView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('check_guest/', CheckGuestView.as_view(), name='check_guest'),
]
