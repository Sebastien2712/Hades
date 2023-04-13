from rest_framework import serializers
from EmployeeApp.models import Employees, Departments

class DepartmentSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields =('DepartmentId', 'DepartmentName')

class EmployeeSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields =('EmployeeId', 'EmployeeName', 'DateOfJoining', 'PhotoFileName', 'Department')