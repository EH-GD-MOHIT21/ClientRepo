from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()



class Department(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name



class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    doctor_image = models.ImageField(upload_to='assets/img/doctors/')
    doctor_title = models.CharField(max_length=40)
    doctor_description = models.TextField()
    doctor_twitter = models.URLField(null=True,blank=True)
    doctor_facebook = models.URLField(null=True,blank=True)
    doctor_instagram = models.URLField(null=True,blank=True)
    doctor_youtube = models.URLField(null=True,blank=True)

    def __str__(self) -> str:
        return self.doctor_name



class Appointment(models.Model):
    patient_name = models.CharField(max_length=60)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=14)
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=60)
    message = models.TextField(null=True,blank=True)
