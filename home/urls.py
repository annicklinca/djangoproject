from django.urls import path
from .import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('',views.welcome, name='home'),
    path('services/',views.services, name='services'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contactus/',views.contactus, name='contactus'),
    path('register/',views.register, name='register'),
    path('paybill/',views.paybill, name='paybill'),
    path('profile/',views.profile, name='profile'),
    path('telepsychiatry/',views.telepsychiatrys, name='telepsychiatry'),
    path('reqtelepsychiatry/',views.telepsychiatrys, name='reqtelepsychiatry'),
    path('registration/',views.registration, name='registration'),
    path('message/',views.message, name='message'),
    path('appointment/',views.appointments, name='appointment')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)