from django.contrib.auth.models import User
from django.db import models


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    title = models.CharField(max_length=60)
    owner = models.ForeignKey(Employer, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()
    time_period = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    assigned_contractor = models.ForeignKey(
        Contractor,
        on_delete=models.SET_NULL,
        null=True,
    )

    @property
    def is_assigned(self):
        return self.assigned_contractor is not None

    def __str__(self):
        return self.title

    @classmethod
    def get_all_data_to_show(cls):
        result = []
        tasks = list(cls.objects.all().order_by("-created_at").values())

        for task in tasks:
            owner = str(Employer.objects.get(pk=task.get("owner_id")))
            task["owner"] = owner
            result.append(task)
        return result
