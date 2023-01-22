from django.shortcuts import render
from django.views.generic import TemplateView

class EmployerPanel(TemplateView):
    template_name = 'employer_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
