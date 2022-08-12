from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('view', views.viewemp, name='viewemp'),
    path('add', views.addemp, name='addemp'),
    path('filter', views.filteremp, name='filteremp'),
    path('delete', views.deleteemp, name='deleteemp'),
    path('delete/<int:emp_id>', views.deleteemp, name='deleteemp'),
]
