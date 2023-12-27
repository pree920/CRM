"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_conveyance, name='view_conveyance'),
    path('record-attendance/', views.record_attendance, name='record_attendance'),
    path('attendance-success/', views.attendance_success, name='attendance_success'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),
    path('edit-attendance/<int:record_id>/', views.edit_attendance, name='edit_attendance'),
    path('delete-attendance/<int:record_id>/', views.delete_attendance, name='delete_attendance'),
    path('employee_analysis/', views.employee_analysis, name='employee_analysis'),
    path('record_empdetails/', views.record_empdetails, name='record_empdetails'),
    path('details_success/', views.details_success, name='details_success'),
    path('leaves/', views.employeeleaves, name='leaves'),
    path('leaves_success/', views.leaves_success, name='leaves_success'),
    path('conveyance_record/', views.conveyance_record, name='conveyance_record'),
    path('conveyance_success/', views.conveyance_success, name='conveyance_success'),
    path('view_conveyance/', views.view_conveyance, name='view_conveyance'),


]
