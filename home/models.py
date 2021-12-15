from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=250)
    category = models.CharField(max_length=255, choices=(('about','about'),('Services','Services'),('Slider','Slider'),('Welcome','Welcome'),('Major Services','Major Services'),('Vision', 'Vision'),('Mission', 'Mission'), ('Docs', 'Docs'),('Services Content', 'Services Content'),('Other services', 'Other services'),('Why','Why choose us?')))
    image=models.FileField(default='')
    body= RichTextField(verbose_name='Body',null=True,blank=True)
    addedon=models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class PatientRegistration(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    parent=models.CharField(max_length=250)
    age=models.IntegerField(max_length=100)
    dateofbirth=models.DateField()
    phone=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    refferedyou=models.CharField(max_length=250)
    hereabout=models.CharField(max_length=250)
    emergencyname=models.CharField(max_length=250)
    emergencyphone=models.CharField(max_length=250)
    emergencyrelationship=models.CharField(max_length=250)
    allergies=models.CharField(max_length=250)
    currentmedication=models.CharField(max_length=250)
    describeproblem=models.CharField(max_length=350)
    interestedin=models.CharField(max_length=250)

    def __str__(self):
        return self.firstname
class messages(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    message=models.CharField(max_length=350)

    def __str__(self):
        return self.name
class appointment(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    date=models.DateField()
    message=models.CharField(max_length=350)
    
    def __str__(self):
        return self.name
class telepsychiatry(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    emailaddress=models.CharField(max_length=250)
    phonenumber=models.CharField(max_length=250)
    dateofbirth=models.DateField()
    fulladdress=models.CharField(max_length=350)
    Signature=models.CharField(max_length=350)
    datesign=models.CharField(max_length=350)
    signer=models.CharField(max_length=350)
    
    def __str__(self):
        return self.firstname