from django.views.generic import ListView, DetailView
from .models import System, Element


class SystemList(ListView):
    template_name = 'helper/main.html'
    model = System
    context_object_name = 'systems'


class SystemDetail(DetailView):
    model = System
    template_name = 'helper/elements.html'

    def get_context_data(self, **kwargs):
        context = super(SystemDetail, self).get_context_data(**kwargs)
        context['elements'] = Element.objects.all()
        return context
