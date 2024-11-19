from django.urls import path
from grade_system import views

urlpatterns = [
    path('student-list/', views.StudentListView.as_view(), name='student-list'),
    path('student-detail/<int:pk>', views.StudentDetailView.as_view(), name='student-detail')
]
