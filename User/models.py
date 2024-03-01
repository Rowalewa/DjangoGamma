from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name


class NextOfKin(models.Model):
    full_name = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=10)
    ID_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
