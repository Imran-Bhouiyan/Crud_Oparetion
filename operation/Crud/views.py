from django.shortcuts import render,redirect, HttpResponse
from .models import Employee
# Create your views here.
def index(request):
    employees=Employee.objects.all()
    context={
        'employees':employees
    }
    return  render(request,'index.html',context)

def create(request):
    print(request.POST)
    name=request.GET['name']
    email=request.GET['email']
    gender=request.GET['gender']
    city=request.GET['city']
    dob=request.GET['dob']
    phone=request.GET['phone']
    employee_details=Employee(name=name,email=email,gender=gender,city=city,dob=dob,phone=phone)
    employee_details.save()
    return redirect('/')


def add_employee(request):
    return render(request,'add_employee.html')

def delete(request,id):
    employees = Employee.objects.get(pk=id)
    employees.delete()
    return redirect('/')


def edit(request,id):
    employees=Employee.objects.get(pk=id)
    context={
        'employees':employees
    }
    return render(request,'edit.html',context)

def update(request,id):
    employees=Employee.objects.get(pk=id)
    name = request.GET['name']
    email = request.GET['email']
    gender = request.GET['gender']
    city = request.GET['city']
    dob = request.GET['dob']
    phone = request.GET['phone']
    employees.save()
    return redirect('/')


