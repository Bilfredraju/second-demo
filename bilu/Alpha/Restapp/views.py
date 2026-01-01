from django.shortcuts import render
from django.db import models
#from django.models import *
from rest_framework.views import APIView
from .serializers import userserializers
from rest_framework.response import Response
from .models import userpro
# Create your views here.

class userprofile(APIView):
    def post(self,req):
        newdata = userserializers(data=req.data)
        if newdata.is_valid():
            newdata.save()
            return Response(newdata.data)
        else:
            return Response("Data Not Valid!")
    def get(self,req):
        profile =userpro.objects.all()
        newdata=userserializers(profile,many=True)
        return Response(newdata.data) 

class profile(APIView):
    def get(self,request,pk):
        profile=userpro.objects.get(id=pk)
        newdata=userserializers(profile)
        return response(new.data)
    def put(self,req,pk):
        profile = userpro.objects.get(id=pk)  
        newdata = userserializers(profile,req.data)
        if newdata.is_valid():
            newdata.save()
            return Response(newdata.data)
        else:
            return Response("Data Not Valid!")

    def delete(self,req,pk):
        profile = userpro.objects.get(id=pk)
        profile.delete()
        return Response("data deleted")            

