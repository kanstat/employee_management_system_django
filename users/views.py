# from crypt import methods
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
    if request.method == "POST":

        namee = request.POST['name']
        deptt = request.POST['dept']
        salaryy = int(request.POST['salary'])
        bonuss = int(request.POST['bonus'])
        rolee = (request.POST['role'])
        phonee = int(request.POST['phone'])
        hire_datee = (request.POST['hire_date'])
        new_empp = employee(name=namee, dept_id=deptt, salary=salaryy,
                            bonus=bonuss, role_id=rolee, phone=phonee, hire_date=hire_datee)
        new_empp.save()
        return HttpResponse('Employee Added Sucessfully')
    elif request.method == "GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An exception has occured")


def filteremp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        all_obj = employee.objects.all()
        if name:
            all_obj = all_obj.filter(name__icontains=name)
        if dept:
            all_obj = all_obj.filter(dept__name=dept)
        if role:
            all_obj = all_obj.filter(role__name=role)
        diction = {
            'all_obj': all_obj
        }
        print
        return render(request, 'view_emp.html', diction)

    elif request.method == "GET":
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Not Found")


def deleteemp(request, emp_id=0):
    if emp_id:
        try:
            emp_removed = employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse("Employee removed sucessfully")
        except:
            return HttpResponse("Please enter valid employee id")
    emps = employee.objects .all()
    context_dic = {
        'emps': emps
    }
    return render(request, 'delete_emp.html', context_dic)
