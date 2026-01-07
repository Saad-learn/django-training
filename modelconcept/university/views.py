from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from datetime import date
from .models import (
    Student,
    Department,
    Course,
    Enrollment,
    StudentProfile,
    GraduateStudent,
    StudentProxy
)

def home(request):
    return HttpResponse("Welcome to University App!")

def create_student(request):
    dept, created = Department.objects.get_or_create(
        name="Computer Science"
    )
    student = Student.objects.create(
        name="saad khan",     # C.F uppercase
        age=21,
        email="saad@gmail.com",
        department=dept      # Many-to-One
    )
    return HttpResponse(f"Student created with ID {student.id}")


def list_students(request):
    students = Student.objects.all()
    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "age": s.age,
            "email": s.email,
            "department": s.department.name
        })
    return JsonResponse(data, safe=False)


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.age = 22
    student.save()
    return HttpResponse("Student updated successfully")


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return HttpResponse("Student deleted successfully")

#many to many
def enroll_student(request):
    student = Student.objects.first()
    course = Course.objects.get_or_create(
        title="Django Development"
    )
    Enrollment.objects.create(
        student=student,
        course=course,
        enrolled_on=date.today(),
        grade="A"
    )
    return HttpResponse("Student enrolled in course with extra fields")


def student_courses(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    courses = student.courses.all()
    course_list = [c.title for c in courses]
    return JsonResponse(course_list, safe=False)

#one to one
def create_student_profile(request):
    student = Student.objects.first()
    profile, created = StudentProfile.objects.get_or_create(
        student=student,
        bio="This is a one-to-one student profile"
    )
    return HttpResponse("Student profile created")


def proxy_student_view(request):
    student = StudentProxy.objects.first()
    if student.is_adult():
        return HttpResponse(f"{student.name} is an adult")
    return HttpResponse(f"{student.name} is not an adult")

#multi Table Inheritence
def create_graduate_student(request):
    dept = Department.objects.first()
    grad = GraduateStudent.objects.create(
        name="Ali",
        age=25,
        email="ali@gmail.com",
        department=dept,
        thesis_title="AI in Healthcare"
    )
    return HttpResponse("Graduate student created")

#abstract base c
def check_timestamps(request):
    student = Student.objects.first()
    return HttpResponse(
        f"Created at: {student.created_at} | Updated at: {student.updated_at}"
    )
