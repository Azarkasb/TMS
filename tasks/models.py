from accounts.models import User
from django.db import models


class Employer(models.Model):
    """person who can create tasks."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Contractor(models.Model):
    """person who can accept and do the tasks"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        PENDING = "P", "تعریف شده"
        ASSIGNED = "A", "واگذار شده"
        DONE = "D", "انجام شده"

    title = models.CharField(max_length=60)
    owner = models.ForeignKey(Employer, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=1,
        default=TaskStatus.PENDING,
        choices=TaskStatus.choices,
    )
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
        """return tasks data for previewing"""
        result = []
        tasks = list(cls.objects.all().order_by("-created_at").values())

        for task in tasks:
            owner = str(Employer.objects.get(pk=task.get("owner_id")))
            state = Task.objects.get(id=task.get("id")).get_state_display()
            task["owner"] = owner
            task["state"] = state
            result.append(task)
        return result

    def assign_contractor(self, contractor: Contractor):
        self.assigned_contractor = contractor
        self.state = Task.TaskStatus.ASSIGNED
        self.save()

    def done(self):
        self.state = Task.TaskStatus.DONE
        self.save()
