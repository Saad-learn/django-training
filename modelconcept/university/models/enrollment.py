from django.db import models

class Enrollment(models.Model):
    student = models.ForeignKey("university.Student", on_delete=models.CASCADE)
    course = models.ForeignKey("university.Course", on_delete=models.CASCADE)
    enrolled_on = models.DateField()
    grade = models.CharField(max_length=2)
