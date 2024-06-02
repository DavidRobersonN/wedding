from django.views.generic import View, TemplateView
from .models import Noiva, Noivo, Padrinho, Madrinha, Casamento, HistoriaDeAmor, Saudacao, NossoBlog
from django.http import Http404, HttpResponse

#########
import tempfile
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML
######

from .models import Guest
from django.shortcuts import render


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
        context['blog'] = NossoBlog.objects.all()
        return context


class CheckGuestView(View):

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")

        if Guest.objects.filter(name=name).exists():
            # Renderizando o conteúdo HTML em string
            html_string = render_to_string('invitation.html', {'name': name})
            pdf_path = '//convite.pdf'  # Caminho absoluto para o diretório onde deseja salvar o arquivo PDF

            try:
                html = HTML(string=html_string)  # Passando essa string que foi gerada para weasyPrint
                html.write_pdf(target=pdf_path)  # Transformando em PDF e criando no diretório especificado

                # Abrindo e retornando o arquivo PDF gerado como resposta HTTP
                with open(pdf_path, 'rb') as pdf_file:
                    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="invitation.pdf"'
                    return response
            except Exception as e:
                return HttpResponse(f'Erro ao gerar o PDF: {e}', status=500)
