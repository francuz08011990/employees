from django.urls import path
from .views import all_employees

urlpatterns = [
    path('', all_employees, name='all_employees')
]