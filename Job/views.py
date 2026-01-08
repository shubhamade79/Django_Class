from django.shortcuts import render
from .models import BangJob,Punejob,BiharJob
# Create your views here.
def BangJob_Views(request):
    data=BangJob.objects.all()
    return render(request,'html/bang.html',{'Data':data})
def PuneJob_Views(request):
    data=Punejob.objects.all()
    return render(request,'html/pune.html',{'Data':data})
def BiharJob_Views(request):
    data=BiharJob.objects.all()
    return render(request,'html/pune.html',{'Data':data})
def index(request):
    return render(request,'html/index.html')