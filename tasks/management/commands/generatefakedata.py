from django.core.management.base import BaseCommand, CommandError
from ._factories import (
    EmployerFactory,
    EmployeeFactory,
    PendingTaskFactory,
    DoneOrAssignedTaskFactory,
)


class Command(BaseCommand):
    help = "Generate a bunch of fake task"

    def handle(self, *args, **options):
        for i in range(9):
            EmployeeFactory.create()
        for i in range(5):
            EmployerFactory.create()
        for i in range(10):
            p = PendingTaskFactory.build()
            d = DoneOrAssignedTaskFactory.build()
            p.save()
            d.save()

        self.stdout.write(self.style.SUCCESS("DONE"))
