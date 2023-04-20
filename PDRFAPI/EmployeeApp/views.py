from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Employees, Departments
from EmployeeApp.serializers import DepartmentSerrializer, EmployeeSerrializer

# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerrializer(departments, many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerrializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failled to Added",safe=False)
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data["DepartmentId"])
        departments_serializer = DepartmentSerrializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Succesfully", safe=False)
    elif request.method == "DELETE":
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Delete Succesfully", safe=False)
    

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            employee = Employees.objects.get(EmployeeId=id)
            employees_serializer = EmployeeSerrializer(employee)
            return JsonResponse(employees_serializer.data,safe=False)
        else:
            employees = Employees.objects.all()
            employees_serializer = EmployeeSerrializer(employees, many=True)
            return JsonResponse(employees_serializer.data,safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerrializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failled to Added",safe=False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data["EmployeeId"])
        employees_serializer = EmployeeSerrializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Succesfully", safe=False)
    elif request.method == "DELETE":
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete Succesfully", safe=False)
