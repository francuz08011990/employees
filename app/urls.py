from django.urls import path
from .views import all_employees, detail_list

urlpatterns = [
    path('', all_employees, name='all_employees'),
    path('detail_list/', detail_list, name='detail_list')
]