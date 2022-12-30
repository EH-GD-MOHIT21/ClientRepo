from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail as _sendmail
import json
from .models import ContactDetails,Doctor,Appointment,Department
import re
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# Create your views here.

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def RenderHome(request):
    doctors = Doctor.objects.all()
    depts = Department.objects.all()
    return render(request,'index.html',{'doctors':doctors,'departments':depts})

@csrf_exempt
def send_mail(request):
    body = json.loads(request.body)
    email = body.get('email')
    name = body.get('name')
    subject = body.get('subject')
    message = body.get('message')
    if re.fullmatch(regex, email):
        model = ContactDetails()
        model.email,model.name,model.subject,model.message = email,name,subject,message
        message = message + f'\n\nContact {name} on {email}.'
        model.save()
        _sendmail(subject=subject,message=message,recipient_list=['experimentallyf@gmail.com'],from_email=settings.EMAIL_HOST_USER)
        return JsonResponse({'status':200,'message':'success'})
    else:
        return JsonResponse({'status':400,'message':'Invalid Email.'})


@csrf_exempt
def BookApointment(request):
    body = json.loads(request.body)
    patient_name = body.get('patient_name')
    patient_email = body.get('patient_email')
    patient_phone = body.get('patient_phone')
    department = body.get('department')
    doctor = body.get('doctor')
    opt_message = body.get('opt_message')
    if re.fullmatch(regex, patient_email):
        model = Appointment()
        model.patient_name,model.patient_email,model.patient_phone = patient_name,patient_email,patient_phone
        model.department,model.doctor,model.message = department,doctor,opt_message
        model.save()
        _sendmail(subject=f'New Appointment Schedule of {patient_name}',message=f'Hey {doctor}!\n\nYou have an appointement request of mr. {patient_name} for department {department}. There message to doctor is: {opt_message}.\n\nFurther You can contact them on mobile {patient_phone} or on email {patient_email}.',recipient_list=['experimentallyf@gmail.com',patient_email],from_email=settings.EMAIL_HOST_USER)
        return JsonResponse({'status':200,'message':'success'})
    else:
        return JsonResponse({'status':400,'message':'Invalid Email.'})