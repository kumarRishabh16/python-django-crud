from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):     #this function will use to add new records and disply the data
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pw)
            reg.save()
            fm=StudentRegistration()

    else:
        fm=StudentRegistration()
    stud =User.objects.all()

    return render(request, 'enroll/addandshow.html',{'form':fm,'student':stud})

def update(request,id): #this will use to update data
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':fm})

def delete_data(request,id):
    if request.method =='POST':
        dele= User.objects.get(pk=id)
        dele.delete()
        return HttpResponseRedirect('/')

