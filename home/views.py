from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.



def welcome(request):
    services=Content.objects.all().filter(category='Services').order_by('-id')[:20]
    welcome = Content.objects.all().filter(category='Welcome').order_by('-id')[:1]
    slider = Content.objects.all().filter(category='Slider').order_by('-id')[:10]
    sliderone = Content.objects.all().filter(category='Slider').order_by('-id')[:1]
    context ={
        'services':services,
        'welcomes':welcome,
        'slides':slider,
        'slideone':sliderone
    }
    return render(request, 'index.html',context)
def services(request):
    services=Content.objects.all().filter(category='Services Content').order_by('-id')[:20]
    service=Content.objects.all().filter(category='Services').order_by('-id')[:20]
    docs = Content.objects.all().filter(category='Docs').order_by('-id')[:5]
    otherservice=Content.objects.all().filter(category='Other services').order_by('-id')[:20]
    context={
        'services':services,
        'docs':docs,
        'servicess':service,
        'otherservices':otherservice
    }
    return render(request, 'services.html',context)    

def aboutus(request):
    about=Content.objects.all().filter(category='about').order_by('-id')[:1]
    services=Content.objects.all().filter(category='Services').order_by('-id')[:20]
    why =Content.objects.all().filter(category='Why').order_by('-id')[:15]
    context={
        'about':about,
        'services':services,
        'why':why
    }
    return render(request, 'aboutus.html',context)

def contactus(request):
    return render(request, 'contactus.html')
    
def register(request):
    return render(request, 'register.html')
    
def paybill(request):
    return render(request, 'paybill.html')
    
def profile(request):
    return render(request, 'profile.html')
def registration(request):
    select =PatientRegistration.objects.all().order_by('id')
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        parent = request.POST['parent']
        age = request.POST['age']
        dateofbirth = request.POST['dateofbirth']
        phone = request.POST['phone']
        email = request.POST['email']
        refferedyou = request.POST['refferedyou']
        hereabout = request.POST['hereabout']
        emergencyname = request.POST['emergencyname']
        emergencyphone = request.POST['emergencyphone']
        emergencyrelationship = request.POST['emergencyrelationship']
        allergies = request.POST['allergies']
        currentmedication = request.POST['currentmedication']
        describeproblem = request.POST['describeproblem']
        interestedin = request.POST['interestedin']
        insert = PatientRegistration(
            firstname=firstname,
            lastname=lastname, 
            parent=parent, 
            age=age, 
            dateofbirth=dateofbirth, 
            phone=phone, 
            email=email, 
            refferedyou=refferedyou, 
            hereabout=hereabout, 
            emergencyname=emergencyname, 
            emergencyphone=emergencyphone, 
            emergencyrelationship=emergencyrelationship, 
            allergies=allergies, 
            currentmedication=currentmedication, 
            describeproblem=describeproblem, 
            interestedin=interestedin
        )
        try:
            insert.save()
            return render(request,'register.html',{'message':'Registration has been inserted successful','data':select})
        except:
            return render(request,'register.html',{'message':'fail to insert','data':select})
    return render(request, 'register.html',{'data':select})

def message(request):
    select =messages.objects.all().order_by('id')
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        insert = messages(
            name=name,
            email=email, 
            phone=phone,
            subject=subject,
            message=message
        )
        try:
            insert.save()
            return render(request,'contactus.html',{'message':'Your Message has been sent, successful','data':select})
        except:
            return render(request,'contactus.html',{'message':'fail to sent message','data':select})
    return render(request, 'contactus.html',{'data':select})

def appointments(request):
    select =appointment.objects.all().order_by('id')
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        message = request.POST['message']
        insert = appointment(
            name=name,
            email=email, 
            phone=phone,
            date=date,
            message=message
        )
        try:
            insert.save()
            return render(request,'index.html',{'message':'Your Message has been sent, successful','data':select})
        except:
            return render(request,'index.html',{'message':'fail to sent message','data':select})
    return render(request, 'index.html',{'data':select})

def telepsychiatrys(request):
    select =telepsychiatry.objects.all().order_by('id')
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailaddress = request.POST['emailaddress']
        phonenumber = request.POST['phonenumber']
        dateofbirth = request.POST['dateofbirth']
        fulladdress = request.POST['fulladdress']
        Signature = request.POST['signature']
        datesign = request.POST['datesign']
        signer = request.POST['signer']
        insert = telepsychiatry(
            firstname=firstname,
            lastname=lastname,
            emailaddress=emailaddress,
            phonenumber=phonenumber,
            dateofbirth=dateofbirth,
            fulladdress=fulladdress,
            Signature=Signature,
            datesign=datesign,
            signer=signer
        )
        try:
            insert.save()
            return render(request,'telepsychiatry.html',{'message':'telepsychiatry has been sent, successful','data':select})
        except:
            return render(request,'telepsychiatry.html',{'message':'fail to sent','data':select})
    return render(request, 'telepsychiatry.html',{'data':select})