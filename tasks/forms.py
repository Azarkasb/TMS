from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task


class SignupForm(UserCreationForm):
    USER_TYPES = [
        ("employer", 'کارفرما'),
        ("employee", 'پیمانکار'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect)
    # email = forms.EmailField(max_length=100, help_text="required")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'time_period', 'cost', 'description')
