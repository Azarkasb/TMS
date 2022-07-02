import factory
from faker import Faker
from accounts.models import User
from tasks.models import Task, Employer, Contractor
from django.contrib.auth.hashers import make_password

f = Faker("fa_IR")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyFunction(lambda: f.name())
    password = factory.LazyFunction(lambda: make_password(f.password()))
    first_name = factory.LazyAttribute(lambda obj: obj.username.split()[0])
    last_name = factory.LazyAttribute(lambda obj: obj.username.split()[1])
    email = factory.LazyFunction(lambda: f.email())


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contractor

    user = factory.SubFactory(UserFactory)


class EmployerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employer

    user = factory.SubFactory(UserFactory)


class PendingTaskFactory(factory.Factory):
    class Meta:
        model = Task

    title = factory.LazyFunction(lambda: f"{f.job()} {f.word()}")
    owner = factory.Iterator(Employer.objects.all())
    cost = factory.LazyFunction(lambda: f.pyint(min_value=1000, max_value=50 * 1000))
    time_period = factory.LazyFunction(lambda: f.pyint(min_value=1, max_value=20))
    description = factory.LazyFunction(lambda: f.paragraph(nb_sentences=7))


class DoneOrAssignedTaskFactory(PendingTaskFactory):
    state = factory.Iterator([Task.TaskStatus.DONE, Task.TaskStatus.ASSIGNED])
    assigned_contractor = factory.Iterator(Contractor.objects.all())
