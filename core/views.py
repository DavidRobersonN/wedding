from django.views.generic import TemplateView
from .models import Noiva, Noivo, Padrinho, Madrinha


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        noivo = Noivo.objects.get(pk=1)
        noiva = Noiva.objects.get(pk=1)
        context['noiva'] = noiva
        context['noivo'] = noivo
        context['padrinhos'] = Padrinho.objects.all()
        context['madrinhas'] = Madrinha.objects.all()
        return context
