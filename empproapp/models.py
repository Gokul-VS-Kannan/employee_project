from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    age=models.IntegerField()
    phoneno=models.BigIntegerField()


#commands to create model class
#pip install mysqlclient
#python manage.py makemigrations
#python manage.py migrate