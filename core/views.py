from django.views.generic import TemplateView
from .models import Noiva, Noivo, Padrinho, Madrinha, Casamento, HistoriaDeAmor, Saudacao, NossoBlog
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            noivo = Noivo.objects.get(pk=1)
        except Noivo.DoesNotExist:
            raise Http404("Nenhum Noivo cadastrado.")
        try:
            noiva = Noiva.objects.get(pk=1)
        except Noiva.DoesNotExist:
            raise Http404("Nenhuma Noiva cadastrada.")

        context['noiva'] = noiva
        context['noivo'] = noivo
        context['saudacao'] = Saudacao.objects.all()
        context['padrinhos'] = Padrinho.objects.all()
        context['madrinhas'] = Madrinha.objects.all()
        context['casamento'] = Casamento.objects.first()
        context['historias'] = HistoriaDeAmor.objects.all()
        context['blog'] = NossoBlog.objects.all()
        return context



