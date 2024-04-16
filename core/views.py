from django.views.generic import TemplateView
from .models import People

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['people'] = People.objects.order_by('?').all()
        return context