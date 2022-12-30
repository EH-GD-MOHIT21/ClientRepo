from django.contrib import admin
from .models import Appointment,ContactDetails,Doctor,Department
# Register your models here.
models = [Appointment,ContactDetails,Doctor,Department]
for model in models:
    admin.site.register(model)