from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    #path('employeeinfo/', views.employeeinfo, name='employeeinfo'),
]