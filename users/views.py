from django.shortcuts import render, HttpResponse

from users.models import employee

# Create your views here.


def home(request):
    return render(request, 'home.html')


def viewemp(request):
    data = employee.objects.all()
    context = {'data': data}
    print(data)
    return render(request, 'view_emp.html', context)


def addemp(request):
    return render(request, 'add_emp.html')


def filteremp(request):
    return render(request, 'filter_emp.html')


def deleteemp(request):
    return render(request, 'delete_emp.html')
