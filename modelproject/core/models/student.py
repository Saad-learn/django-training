from django.db import models
from .department import Department

class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 15
        super().__init__(*args, **kwargs)

class Student(models.Model):
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    email = models.EmailField(unique=True)
    phone = PhoneField(blank=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='students'
    )

    courses = models.ManyToManyField(
        'Course',
        through='Enrollment',
        related_name='students'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
