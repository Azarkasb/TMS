from django.contrib import admin

from .models import Task, Contractor, Employer


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    pass
