from django.db import models

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now=True)
    grade = models.CharField(max_length=2, blank=True)

    class Meta:
        unique_together = ('student', 'course')
