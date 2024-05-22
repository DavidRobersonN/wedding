from django.views.generic import TemplateView
from .models import Noiva, Noivo, Padrinho, Madrinha, Casamento, HistoriaDeAmor, Saudacao
from django.http import Http404

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RSVPForm

def rsvp_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Envia o e-mail
            send_mail(
                'RSVP Confirmation',
                f'Thank you for your RSVP, {name}! We look forward to seeing you at the event.',
                'your-email@example.com',  # Substitua pelo seu e-mail
                [email],  # E-mail do destinatário
                fail_silently=False,
            )

            return redirect('rsvp_thanks')  # Redireciona para uma página de agradecimento
    else:
        form = RSVPForm()

    return render(request, 'rsvp.html', {'form': form})


class IndexView(TemplateView):
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
        return context
