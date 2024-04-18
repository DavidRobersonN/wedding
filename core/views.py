from django.views.generic import TemplateView
from .models import Padrinho, Noiva, Noivo

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['noiva'] = Noiva.objects.first()
        context['noivo'] = Noivo.objects.first()
        return context