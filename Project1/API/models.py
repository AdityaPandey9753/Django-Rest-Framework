from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  roll = models.IntegerField()
  city = models.CharField(max_length=100)
  
""" Create a model named student with fields name, roll and city
Perform makemigartions and migrate command to register the model
then create a super user to add data in the model
Then create serializer class (open serializer.py)"""