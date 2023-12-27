# myapp/models.py

from django.db import models
from django.contrib.auth.models import User  # Import User model

class Attendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    entry_time = models.TimeField(null=True, blank=True)
    exit_time = models.TimeField(null=True, blank=True)
   
class Employeedetails(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    emp_id =models.IntegerField(default=0)
    bg_grp =models.CharField(max_length=4,default="default", null=True)
    Age = models.IntegerField(default=0)
    role =models.CharField(max_length=64,default="default", null=True)
    experience =models.CharField(max_length=15,default="default", null=True)
    contact =models.CharField(max_length=13,default="default", null=True)
    mail_id =models.CharField(max_length=48,default="default", null=True)


class Employeeleaves(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    sl =models.IntegerField()
    cl =models.IntegerField()
    el =models.IntegerField()
    remark =models.CharField(max_length=200,default="default",null=True)


    
class Inventory(models.Model):
    product_des = models.CharField(max_length=200,null=True)
    partcode = models.CharField(max_length=30,null=True)
    hsncode =models.BigIntegerField()
    price =models.BigIntegerField()
    qty =models.IntegerField()
    remarks =models.CharField(max_length=150,null=True)
    

class Conveyance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField()
    company_name = models.CharField(max_length = 100)
    Transport_mode = models.CharField(max_length = 20)
    Kms = models.IntegerField()
    








    

