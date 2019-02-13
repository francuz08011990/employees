from django.shortcuts import render
from .models import Profile


def all_employees(request):
    employees_list = Profile.objects.filter(chief=None)
    data = {'employees': employees_list}
    return render(request, 'index.html', data)


def detail_list(request):
    employees = Profile.objects.all()
    data = {'employees': employees}
    return render(request, 'detail_list.html', data)
