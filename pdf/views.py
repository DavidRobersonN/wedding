from django.views.generic import TemplateView
from django.shortcuts import render
from core.models import Noivo, Noiva, Casamento, Convidados
from django.http import HttpResponse
# Create your views here.
"""
class ConviteView(TemplateView):
    template_name = 'convite.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noivo'] = Noivo.objects.get(pk=1)
        context['noiva'] = Noiva.objects.get(pk=1)
        context['casamento'] = Casamento.objects.first()
        return context
"""
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
