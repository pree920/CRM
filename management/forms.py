


from django.contrib.auth.models import User
from django import forms
from .models import Attendance,Employeedetails,Employeeleaves,Inventory,Conveyance
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'entry_time', 'exit_time']

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = User.objects.all()
        self.fields['date'].widget.attrs.update({'id': 'datepicker'})
        self.fields['entry_time'].widget.attrs.update({'id': 'timepicker'})
        self.fields['entry_time'].required = False  # Make entry_time not required
        self.fields['exit_time'].required = False  # Make exit_time not required

class EmployeedetailsForm(forms.ModelForm):
    class Meta:
        model = Employeedetails
        fields = ['employee','emp_id', 'bg_grp', 'Age', 'role','experience','contact','mail_id']

    def __init__(self, *args, **kwargs):
        super(EmployeedetailsForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = User.objects.all()
        self.fields['emp_id'].required = False  # Make entry_time not required
        self.fields['bg_grp'].required = False  
        self.fields['Age'].required = False 
        self.fields['role'].required = False 
        self.fields['contact'].required = False 
        self.fields['mail_id'].required = False 



class EmployeeleavesForm(forms.ModelForm):
    class Meta:
        model = Employeeleaves
        fields = ['employee','cl','sl','el','remark']

    def __init__(self, *args, **kwargs):
        super(EmployeeleavesForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = User.objects.all()
        self.fields['cl'].required = False  # Make entry_time not required
        self.fields['sl'].required = False  
        self.fields['el'].required = False 
        self.fields['remark'].required = False 
        
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_des','partcode','hsncode','price','qty','remarks']

    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['product_des'].queryset = User.objects.all()
        self.fields['partcode']
        self.fields['hsncode'].required = False  
        self.fields['price']
        self.fields['qty']
        self.fields['remarks']

class ConveyanceForm(forms.ModelForm):
    class Meta:
        model = Conveyance
        fields = ['employee','Date','company_name','Transport_mode','Kms']

    def __init__(self, *args, **kwargs):
        super(ConveyanceForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = User.objects.all()
        self.fields['Date'].widget.attrs.update({'id': 'datepicker'})
        self.fields['company_name']
        self.fields['Transport_mode']
        self.fields['Kms']
        
       




        
  




