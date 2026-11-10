from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    employees = Employee.objects.all()
    employees_expensive = Employee.objects.filter(salary__gt=3000)
    employees_most_expensive_count = Employee.objects.filter(salary__gte=5000).count()
    sales_employees = Employee.objects.filter(department__name='Sales')
    sales_dep_salary = sales_employees.aggregate(average_sales_salary = Avg('salary'))
    employees_hired_january = Employee.objects.filter(hire_date__lt=date(2022, 1, 1)).exclude(department__name='HR')

    ctx = {'employees':employees,
           'employees_expensive':employees_expensive,
           'employees_most_expensive_count':employees_most_expensive_count,
           'average_sales_salary':sales_dep_salary['average_sales_salary'],
           'employees_hired_january':employees_hired_january}

    return render(request, 'employee_list.html', ctx)
