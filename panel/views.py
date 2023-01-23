from django.views.generic import TemplateView
from tasks.models import Task, Employer, Contractor
from .permissions import EmployerPermissionMixin, ContractorPermissionMixin


class EmployerPanel(EmployerPermissionMixin, TemplateView):
    template_name = 'employer_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employer = Employer.objects.get(user=self.request.user)
        context['pending_tasks'] = Task.objects.filter(owner=employer, state='P')
        context['assigned_tasks'] = Task.objects.filter(owner=employer, state='A')
        context['done_tasks'] = Task.objects.filter(owner=employer, state='D')
        return context


class ContractorPanel(ContractorPermissionMixin, TemplateView):
    template_name = 'contractor_tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contractor = Contractor.objects.get(user=self.request.user)
        context['assigned_tasks'] = Task.objects.filter(assigned_contractor=contractor, state='A')
        context['done_tasks'] = Task.objects.filter(assigned_contractor=contractor, state='D')
        return context
