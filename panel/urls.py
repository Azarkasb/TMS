from django.urls import path
from panel import views

app_name = 'panel'
urlpatterns = [
    path("", views.EmployerPanel.as_view(), name='employer_panel')
]