from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Students
    path('students/', views.view_students, name='view_students'),
    path('manage_student/', views.manage_student, name='add_student'),
    path('manage_student/<int:student_id>/', views.manage_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    # Staff
    path('staff/', views.view_staff, name='view_staff'),
    path('manage_staff/', views.manage_staff, name='add_staff'),
    path('manage_staff/<int:staff_id>/', views.manage_staff, name='edit_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
]
