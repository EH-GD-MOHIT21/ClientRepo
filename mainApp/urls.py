from django.urls import path
from . import views

urlpatterns = [
    path('',views.RenderHome),
    path('sendmail',views.send_mail),
    path('book',views.BookApointment),
]
