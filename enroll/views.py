import email
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from enroll.forms import StudentRegistartion
from enroll.models import User

# Create your views here.
#this function is for adding new item an show item
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistartion(request.POST)
     if fm.is_valid():
        nm=fm.cleaned_data['name']
        em=fm.cleaned_data['email']
        pw=fm.cleaned_data['password']
        reg=User(name=nm,email=em,password=pw)
        reg.save()
        fm = StudentRegistartion()     
    # we can use this method also fm.save()
    else:    
     fm = StudentRegistartion()
    stud = User.objects.all()
    # stud ko else ke baher lagana chahiye
    return render(request,'enroll/addshow.html',{'form':fm,'stu':stud})

#update
def update(request,id):
    if request.method =="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistartion(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistartion(instance=pi) 
    return render(request,'enroll/update.html',{'form':fm})
    # request.method =="POST":
        

# delete function
def delete(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')