from django.views.generic import TemplateView

from pdf.views import ConviteView
from .models import Noiva, Noivo, Padrinho, Madrinha, Casamento, HistoriaDeAmor, Saudacao, NossoBlog, Convidados
from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


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

def render_convite(request, nome, noivo, noiva, casamento):
    context = {
        'nome': nome,
        'noivo': noivo,
        'noiva': noiva,
        'casamento': casamento,
    }
    return render(request, 'convite.html', context)

class Formulario(TemplateView):
    template_name = 'convite.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()

        if not name:
            return render(request, self.template_name, {'error_message': 'Por favor, insira um nome válido.'})

        if Convidados.objects.filter(nome=name).exists():
            try:
                noivo = Noivo.objects.get(pk=1)
                noiva = Noiva.objects.get(pk=1)
                casamento = Casamento.objects.first()
                return render_convite(request, name, noivo, noiva, casamento)
            except (Noivo.DoesNotExist, Noiva.DoesNotExist):
                return HttpResponse("Noivo ou Noiva não encontrados")
        else:
            return render(request, self.template_name, {'error_message': 'Desculpe, você não está na lista de convidados.'})
