from django.db import models
from .base import CommonInfo, UpperCaseField
from .course import Course
from .enrollment import Enrollment

class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name="Department Name")
    def __str__(self):
        return self.name

class Student(CommonInfo):
    name = UpperCaseField(max_length=50, verbose_name="Student Name")
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    department = models.ForeignKey("university.Department",on_delete=models.CASCADE)
    courses = models.ManyToManyField("university.Course",through=Enrollment)
    def __str__(self):
        return self.name

class GraduateStudent(Student):
    thesis_title = models.CharField(max_length=200)


