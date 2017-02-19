from django.views.generic import ListView, DetailView
from .models import System, Element


class SystemList(ListView):
    template_name = 'helper/main.html'
    model = System
    context_object_name = 'systems'


class ElementList(ListView):
    template_name = 'helper/elements.html'
    context_object_name = 'elements'

    def get_queryset(self):
        return Element.objects.filter(system_id=self.kwargs['sys_id'])

