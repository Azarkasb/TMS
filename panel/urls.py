from django.urls import path
from panel import views

urlpatterns = [
    path("", views.EmployerPanel.as_view(), name='employer_panel')
]