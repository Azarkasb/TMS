from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

from tasks.models import Contractor, Employer


class EmployerPermissionMixin(AccessMixin):
    """User should be authenticated and be an employer"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/tasks/login-required/')
        if not Employer.objects.filter(user=request.user).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ContractorPermissionMixin(AccessMixin):
    """User should be authenticated and be a contractor"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/tasks/login-required/')
        if not Contractor.objects.filter(user=request.user).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
