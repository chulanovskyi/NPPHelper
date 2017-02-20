from django.views.generic import ListView, DetailView
from .models import System, Element


class SystemList(ListView):
    template_name = 'helper/main.html'
    model = System
    context_object_name = 'systems'


class SystemDetail(DetailView):
    template_name = 'helper/system_detail.html'
    context_object_name = 'system'
    model = System
    slug_url_kwarg = 'sys_slug'


class ElementDetail(DetailView):
    template_name = 'helper/element_detail.html'
    context_object_name = 'element'
    model = Element
    slug_url_kwarg = 'elem_slug'


