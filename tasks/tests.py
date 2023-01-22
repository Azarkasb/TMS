from django.test import TestCase, Client
from .models import Employer, Contractor


class TestUserRegistering(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registering_employer(self):
        response = self.client.post(
            "tasks/register/",
            data={
                "username": "Ali",
                "email": "Ali@tms.com",
                "password1": "IAmAli2023",
                "password2": "IAmAli2023",
                "user_type": "employer",
            },
            format="json",
        )
        employer = Employer.objects.get(user__username="Ali")
        self.assertEqual(employer.user.email, "Ali@tms.com")
        self.assertEqual(employer.user.is_employer, True)

    def test_registering_contractor(self):
        self.client.post(
            "tasks/register/",
            data={
                "username": "Javad",
                "email": "Javad@tms.com",
                "password1": "IAmJavad2023",
                "password2": "IAmJavad2023",
                "user_type": "contractor",
            },
            format="json",
        )
        contractor = Contractor.objects.get(user__username="Javad")
        self.assertEqual(contractor.user.email, "Javad@tms.com")
        self.assertEqual(contractor.user.is_employee, True)
