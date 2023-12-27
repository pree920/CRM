


from django.shortcuts import render, redirect
from .forms import AttendanceForm,EmployeedetailsForm,EmployeeleavesForm,InventoryForm,ConveyanceForm
from .models import Attendance,Employeedetails,Employeeleaves,Inventory,Conveyance
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import F, ExpressionWrapper, fields, Avg,Count
from django.core.serializers import serialize
from django.http import JsonResponse
import json
from django.contrib import admin
from .models import Employeeleaves
from datetime import date, timedelta
from django.db.models.functions import TruncMonth

admin.site.register(Employeeleaves)
admin.site.register(Employeedetails)


def record_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            entry_time = form.cleaned_data.get('entry_time')
            exit_time = form.cleaned_data.get('exit_time')
            if entry_time is None and exit_time is None:
                entry_time = None
                exit_time = None

            # Create or update the attendance record
            selected_employee = form.cleaned_data['employee']
            date = form.cleaned_data['date']
            attendance, created = Attendance.objects.get_or_create(
                employee=selected_employee,
                date=date,
                defaults={
                    'entry_time': entry_time,
                    'exit_time': exit_time
                }
            )
            return redirect('attendance_success')  # Redirect to a success page
    else:
        form = AttendanceForm()

    return render(request, 'record_attendance.html', {'form': form})


def attendance_success(request):
    return render(request, 'attendance_success.html')

def view_attendance(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        if employee_id:
            selected_employee = User.objects.get(pk=employee_id)
            attendance_records = Attendance.objects.filter(employee=selected_employee)
        else:
            selected_employee = None
            attendance_records = None
    else:
        selected_employee = None
        attendance_records = None

    employees = User.objects.all()  # Assuming User is the employee model

    return render(request, 'view_attendance.html', {
        'employees': employees,
        'selected_employee': selected_employee,
        'attendance_records': attendance_records,
    })
def edit_attendance(request, record_id):
    attendance_record = get_object_or_404(Attendance, id=record_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance_record)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    else:
        form = AttendanceForm(instance=attendance_record)

    return render(request, 'edit_attendance.html', {'form': form})

def delete_attendance(request, record_id):
    attendance_record = get_object_or_404(Attendance, id=record_id)
    attendance_record.delete()
    return redirect('view_attendance')




def employee_analysis(request):
    employee_id = request.GET.get('employee_id')
    selected_employee = get_object_or_404(User, pk=employee_id) if employee_id else None
    
       # Calculate date range for the last 7 days
    today = date.today()
    seven_days_ago = today - timedelta(days=7)

    daily_avg = Attendance.objects.annotate(
        time_diff=ExpressionWrapper(
            F('exit_time') - F('entry_time'),
            output_field=fields.DurationField()
        )
    ).filter(
        employee=selected_employee,
        date__gte=seven_days_ago  # Filter for the last 7 days
    ).values('date').annotate(avg_hours=Avg('time_diff')).order_by('date')

    dates = ','.join(['"{}"'.format(entry['date'].strftime('%Y-%m-%d')) for entry in daily_avg])

    avg_hours = [entry['avg_hours'].total_seconds() / 3600 for entry in daily_avg]
    avg_hours_str = ','.join(['"{}"'.format(avg) for avg in avg_hours])
    last_30_attendance = Attendance.objects.filter(employee=selected_employee).order_by('-date')[:30]

    
    employee_details = Employeedetails.objects.get(employee=selected_employee) if selected_employee else None
    
    emp_id = bg_grp = Age = role = experience = contact = mail_id = None
    if employee_details:
        emp_id = employee_details.emp_id
        bg_grp = employee_details.bg_grp
        Age = employee_details.Age
        role = employee_details.role
        experience = employee_details.experience
        contact = employee_details.contact
        mail_id = employee_details.mail_id
    
    cl = sl = el = remark = None
    employee_leaves = Employeeleaves.objects.filter(employee=selected_employee).order_by('-id').first() if selected_employee else None
    if employee_leaves:
        cl = employee_leaves.cl
        sl = employee_leaves.sl
        el = employee_leaves.el
        remark = employee_leaves.remark

    # Calculate date ranges for the current month, previous month, and month before that
    today = date.today()
    current_month_start = today.replace(day=1)
    last_month_end = current_month_start - timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)
    two_months_ago_end = last_month_start - timedelta(days=1)
    two_months_ago_start = two_months_ago_end.replace(day=1)

    # Aggregate attendance data for the current month, previous month, and month before that
    attendance_current_month = Attendance.objects.filter(
        employee=selected_employee,
        date__year=today.year,
        date__month=today.month
    ).values('date').annotate(unique_days=Count('date', distinct=True))

    attendance_previous_month = Attendance.objects.filter(
        employee=selected_employee,
        date__year=last_month_start.year,
        date__month=last_month_start.month
    ).values('date').annotate(unique_days=Count('date', distinct=True))

    attendance_two_months_ago = Attendance.objects.filter(
        employee=selected_employee,
        date__year=two_months_ago_start.year,
        date__month=two_months_ago_start.month
    ).values('date').annotate(unique_days=Count('date', distinct=True))

    data = {
        'dates': dates,
        'avg_hours': avg_hours_str,
        'currentuser': selected_employee.username if selected_employee else None,
        'emp_id': emp_id,
        'bg_grp': bg_grp,
        'Age': Age,
        'role': role,
        'experience': experience,
        'contact': contact,
        'mail_id': mail_id,
        'cl': cl,
        'sl': sl,
        'el': el,
        'remark': remark,
        'attendance_data_current_month': len(attendance_current_month),
        'attendance_data_previous_month': len(attendance_previous_month),
        'attendance_data_two_months_ago': len(attendance_two_months_ago),
        'last_30_attendance':last_30_attendance,
    }

    return render(request, "employee_analysis.html", data)



def record_empdetails(request):
    if request.method == 'POST':
        form = EmployeedetailsForm(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data.get('emp_id')
            bg_grp = form.cleaned_data.get('bg_grp')
            Age = form.cleaned_data.get('Age')  # Modified variable name to lowercase 'age'
            role = form.cleaned_data.get('role')
            experience = form.cleaned_data.get('experience')
            contact = form.cleaned_data.get('contact')
            mail_id = form.cleaned_data.get('mail_id')
            
            # Create or update the employee details
            selected_employee = form.cleaned_data['employee']
            # Consider the way to retrieve 'date' for employee details, perhaps it's associated with their employment start date.
            # For now, let's assume the date is not necessary for this scenario.
            
            # Update or create the employee details in the database
            employee_details, created = Employeedetails.objects.get_or_create(
                employee=selected_employee,
                defaults={
                    'emp_id': emp_id,
                    'bg_grp': bg_grp,
                    'Age': Age,
                    'role': role,
                    'experience': experience,
                    'contact': contact,
                    'mail_id': mail_id
                }
            )
            return redirect('details_success')  # Redirect to a success page for employee details
    else:
        form = EmployeedetailsForm()

    return render(request, 'details.html', {'form': form})

def details_success(request):
    return render(request, 'details_success.html')

def employeeleaves(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            product_des = form.cleaned_data.get('product_des')
            partcode = form.cleaned_data.get('partcode')
            hsncode = form.cleaned_data.get('hsncode')
            price = form.cleaned_data.get('price')
            qty = form.cleaned_data.get('qty')
            remarks = form.cleaned_data.get('remarks')


          
            # Consider the way to retrieve 'date' for employee details, perhaps it's associated with their employment start date.
            # For now, let's assume the date is not necessary for this scenario.
            
            # Update or create the employee details in the database
            Inventory_item, created = Inventory.objects.get_or_create(
               
                defaults={
                    'product_des': product_des,
                    'partcode': partcode,
                    'hsncode': hsncode,
                    'price': price,
                    'qty': qty,
                    'remarks': remarks,
                
                    
                }
            )
            return redirect('leaves_success')  # Redirect to a success page for employee details
    else:
        form = InventoryForm()

    return render(request, 'leaves.html', {'form': form})
def leaves_success(request):
    return render(request, 'leaves_success.html')


def conveyance_record(request):
    if request.method == 'POST':
        form = ConveyanceForm(request.POST)
        print("request method")
        try:
            if form.is_valid():
                print("form is valid")
               
                company_name = form.cleaned_data.get('company_name')
                Transport_mode = form.cleaned_data.get('Transport_mode')
                kms = form.cleaned_data.get('Kms')
              

                selected_employee = form.cleaned_data['employee']
                Date = form.cleaned_data['Date']
                Conveyance_item, created = Conveyance.objects.get_or_create(
                    employee=selected_employee,
                    Date=Date,
                    defaults={
                        'Date': Date,
                        'company_name': company_name,
                        'Transport_mode': Transport_mode,
                        'Kms': kms,
                        
                    }
                )
                return redirect('conveyance_success')  # Redirect to a success page
            else:
                # Handle form validation errors
                # You might want to pass the form with errors back to the template
                return render(request, 'conveyance_record.html', {'form': form})
        except Exception as e:
            print(f"An error occurred: {e}")
            # Handle the error appropriately, such as logging it
            # You might want to render an error page here
    else:
        form = ConveyanceForm()
        print("form invalid")
    
    return render(request, 'conveyance_record.html', {'form': form})

def conveyance_success(request):
    return render(request, 'conveyance_success.html')

def view_conveyance(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        if employee_id:
            selected_employee = User.objects.get(pk=employee_id)
            conveyance_records = Conveyance.objects.filter(employee=selected_employee)
        else:
            selected_employee = None
            conveyance_records = None
    else:
        selected_employee = None
        conveyance_records = None

    employees = User.objects.all()  # Assuming User is the employee model

    return render(request, 'view_conveyance.html', {
        'employees': employees,
        'selected_employee': selected_employee,
        'conveyance_records': conveyance_records,
    })