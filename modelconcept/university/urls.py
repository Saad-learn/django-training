from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_student, name='create_student'),
    path('list/', views.list_students, name='list_students'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('courses/<int:student_id>/', views.student_courses, name='student_courses'),
    path('profile/', views.create_student_profile, name='create_student_profile'),
    path('proxy/', views.proxy_student_view, name='proxy_student'),
    path('graduate/', views.create_graduate_student, name='create_graduate_student'),
    path('timestamps/', views.check_timestamps, name='check_timestamps'),
]
