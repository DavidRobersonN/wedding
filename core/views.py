from django.views.generic import TemplateView
from .models import Noivo, Noiva

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['noivo'] = Noivo.objects.first()
        context['noiva'] = Noiva.objects.first()
        return context