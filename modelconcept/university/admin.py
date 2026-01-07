# Correct admin.py
from django.contrib import admin
from .models import (
    Student,
    Department,
    Course,
    Enrollment,
    StudentProfile,
    GraduateStudent,
    StudentProxy
)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(StudentProfile)
admin.site.register(GraduateStudent)
admin.site.register(StudentProxy)
