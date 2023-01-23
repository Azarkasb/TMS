from django.urls import path
from panel import views

app_name = 'panel'
urlpatterns = [
    path("/employer", views.EmployerPanel.as_view(), name='employer_panel'),
    path("/contractor", views.ContractorPanel.as_view(), name='contractor_panel')
]
