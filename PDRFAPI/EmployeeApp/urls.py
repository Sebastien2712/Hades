from django.urls import path
from EmployeeApp import views


urlpatterns = [
    path("api/departments/", views.departmentApi),
    path("api/departments/<int:id>", views.departmentApi),
    path("api/employees/", views.employeeApi),
    path("api/employees/<int:id>", views.employeeApi)
]
