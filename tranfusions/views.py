from django.contrib import messages
from django.shortcuts import render
from .models import tranfusion
# Create your views here.
def tranfusionsHome(request):
    if request.method == 'POST':
        print('post request detected ')
        employee_id = request.POST['emp_id']
        date =request.POST['date']
        time = request.POST['time']
        patient_id = request.POST['patient_id']
        patient_name = request.POST['patient_name']
        blood_product_type = request.POST['blood_product_type']
        blood_product_id = request.POST['blood-product-id']
        print(employee_id,date,time,patient_id,patient_name,blood_product_id,blood_product_type)
        tranfusion_event = tranfusion(
            employee_id = employee_id, 
            date = date, 
            time = time, 
            patient_id = patient_id, 
            patient_name = patient_name,
            blood_product_type = blood_product_type,
            blood_product_id = blood_product_id
            )
        tranfusion_event.save()
        messages.success(request, "Tranfusion event added successfully")

    return render(request, 'tranfusion.html')