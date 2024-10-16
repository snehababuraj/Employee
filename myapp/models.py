from django.db import models
class Employee(models.Model):

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    location=models.CharField(max_length=200)

    email=models.EmailField(max_length=200)

    address=models.CharField(max_length=200)

    def __str__(self):

        return self.name
