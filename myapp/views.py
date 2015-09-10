from django.shortcuts import render
from django.views.generic import TemplateView

from .tasks import hello_world, calculo


class IndexView(TemplateView):
    template_name = 'template/index.html'

    def get_context_data(self,**kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        calculo.delay()
        hello_world.delay()
        return context

