from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Student
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializers import StudentSerializer
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.
class TestViewset(ViewSet):
    def list(self,request):
        std=Student.objects.all()
        Serializer = StudentSerializer(std,many=True)
        return Response(Serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        Serializer = StudentSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({'msg':'data saved!'})
        else:
            return Response(Serializer.errors)
    
    def retrieve(self,request,pk):
        try:
            std = Student.objects.get(pk=pk)
            Serializer = StudentSerializer(instance=std)
            return Response(Serializer.data)
        except Student.DoesNotExist:
            return Response({'msg':'id does not exist!'})
    def update(self,request,pk):
        try:
            std = Student.objects.get(pk=pk)
            Serializer = StudentSerializer(instance=std,data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                return Response({'msg':'data updated'})
            else:
                return Response(Serializer.errors)
        except Student.DoesNotExist:
            return Response({'msg':'id does not exist!'})

    def destroy(self,request,pk):
        try:
            std = Student.objects.get(pk=pk)
            std.delete()
            return Response({'msg':'data deleted!'})
        except Student.DoesNotExist:
            return Response({'msg':'id does not exist!'})
        




