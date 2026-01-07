from django.contrib import admin
from .models import (
    Department,
    Student,
    Course,
    Enrollment
)
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_field = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_dispay = ('code', 'title', 'credits',)
    search_fields = ('title', 'code',)
    list_filter = ('credits',)

class EnrollmentInnline(admin.TabularInline):
    model = Enrollment
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'department'
    )
    list_filter = ('department',)
    search_fields = ('first_name', 'last_name', 'email',)
    inlines = [EnrollmentInnline]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'course',
        'enrollment_date',
        'grade'
    )
    list_filter = ('course', 'grade',)
    search_fields = ('student__first_name', 'studnet__last_name',)
