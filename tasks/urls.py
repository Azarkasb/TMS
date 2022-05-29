from django.urls import path
from tasks import views

app_name = "tasks"
urlpatterns = [
    path("<int:task_id>/", views.detail, name="detail"),
    path('new-task/', views.new_task, name="new-task"),
    path('assign-task/<int:task_id>/', views.assign_task, name="assign-task"),
    path("register/", views.register, name="register"),
    path("login-required/", views.login_required_error, name="login-required"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
