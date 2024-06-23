from django.views.generic import TemplateView

from core.models import Noivo, Noiva, Casamento


# Create your views here.

class ConviteView(TemplateView):
    template_name = 'convite.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noivo'] = Noivo.objects.get(pk=1)
        context['noiva'] = Noiva.objects.get(pk=1)
        context['casamento'] = Casamento.objects.first()
        return context
