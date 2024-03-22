from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail,
                        EmpDesignation=EmpDesignation)
        data.save()

        return redirect('show-emp')
    else:
        return render(request, 'insert.html')
from django.contrib.auth.decorators import login_required
@login_required(login_url='home1')
def show_emp(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})

# Update Employee

def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            employees.EmpName = request.POST['EmpName']
            employees.EmpGender = request.POST['EmpGender']
            employees.EmpEmail = request.POST['EmpEmail']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.save()
            return redirect('show-emp')
    context = {
        'employees': employees,
    }

    return render(request,'edit.html',context)

#Delete Employee
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee

def remove_emp(request, pk):
    try:
        employee = get_object_or_404(Employee, id=pk)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found", status=404)

    if request.method == 'POST':
        employee.delete()
        return redirect('show-emp')

    context = {
        'employee': employee,
    }

    return render(request, 'delete.html', context)

'''
insert.html
delete.html
edit.html
show.html
'''