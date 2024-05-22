from django.urls import path
from django.views.generic import TemplateView

from . views import IndexView, rsvp_view


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rsvp/', rsvp_view, name='rsvp'),
    path('rsvp/thanks/', TemplateView.as_view(template_name="thanks.html"), name='rsvp_thanks'),
]
