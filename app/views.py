from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Profile


def all_employees(request):
    employees_list = Profile.objects.filter(chief=None)
    data = {'employees': employees_list}
    return render(request, 'index.html', data)


def detail_list(request):
    queryset = Profile.objects.all()

    sort_by = request.GET.get("sort_by")
    if sort_by:
        queryset = queryset.order_by(sort_by)
    search = request.POST.get('search')
    if search:
        queryset = queryset.filter(
            Q(last_name__icontains=search) |
            Q(first_name__icontains=search) |
            Q(middle_name__icontains=search) |
            Q(position__icontains=search)
        )
    paginator = Paginator(queryset, 25)
    page = request.GET.get('page')
    employees = paginator.get_page(page)
    data = {'employees': employees, 'sort_by': sort_by, 'search': search, 'page': page}
    return render(request, 'detail_list.html', data)
