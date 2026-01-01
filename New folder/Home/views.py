from django.shortcuts import render,redirect
from django.http import HttpResponse
from Home import urls
# Create your views here.

def landingpage(req):
    return render(req,'Land.html')
def homecall(req):
    return render(req,"index.html")

def add(req):
    if req.method=="POST":
       val1=req.POST['num1']
       val2=req.POST['num2']
       res=int(val1)+int(val2)
       return render(req,"result.html",{'result':res})
    return render(req,"add.html")   

def land(req):
    return render(req,'Land.html')