from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('reports/', views.reports, name='reports'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('all-students/', views.all_students, name='all_students'),
    path('students-by-field/<str:field_name>/', views.students_by_field, name='students_by_field'),
    path('students-by-year/<int:year>/', views.students_by_year, name='students_by_year'),

]
