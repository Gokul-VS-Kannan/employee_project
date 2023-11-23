from django.test import TestCase
from empproapp.models import Employee

class TestModel(TestCase):
    def testModelEmployee(self):
        emp = Employee.objects.create(name='Ben',age=25,phoneno=9207456646,address='kollam')
        print(emp)
        self.assertIsInstance(emp,Employee)