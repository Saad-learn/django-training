from django.db import models
from .student import Student

class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )
    bio = models.TextField()
    def __str__(self):
        return self.student.name
