from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

from .models import Task


class SignupForm(UserCreationForm):
    USER_TYPES = [
        ("employer", "کارفرما"),
        ("employee", "پیمانکار"),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "user_type")


class TaskForm(forms.ModelForm):
    MAX_COST = 50 * 1000
    MIN_COST = 1 * 1000

    class Meta:
        model = Task
        fields = ("title", "time_period", "cost", "description")

    def clean_cost(self):
        cost = self.cleaned_data["cost"]
        if cost <= self.MIN_COST or cost >= self.MAX_COST:
            msg = f"Cost is not in valid range ({self.MIN_COST}, {self.MIN_COST})"
            raise forms.ValidationError(msg)
        return cost

    def clean(self):
        super().clean()
        cost = self.cleaned_data["cost"]
        time_period = self.cleaned_data["time_period"]
        if cost > 30 * 1000 and time_period < 3:
            msg = "حداکثر قیمت کارها بازمان کمتر از سه روز ۳۰۰۰۰ تومان است"
            raise forms.ValidationError(msg)
        return self.cleaned_data
