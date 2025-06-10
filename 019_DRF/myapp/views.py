from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from myapp.serializer import *

# Create your views here.
@api_view(['GET'])
def index(request):
    allstudent = student.objects.all()
    ser = studentserializer(allstudent,many=True)
    return Response({"students":ser.data})

@api_view(['POST'])
def add(request):
    try:
        ser = studentserializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"somthing went wrong"})
        else : 
            ser.save()
            return Response({"data":ser.data,"mesasge":"data added successfully"})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})
    

@api_view(['PUT'])
def update(request,id):
    try:     
        studentbyid = student.objects.get(pk=id)
        ser = studentserializer(studentbyid,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"somthing went wrong"})
        else : 
            ser.save()
            return Response({"data":ser.data,"mesasge":"data updated successfully"})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})
    

@api_view(['DELETE'])
def delete(request,id):
    try:     
        studentbyid = student.objects.get(pk=id)
        studentbyid.delete()
        return Response({"success":True})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})
    
@api_view(['GET'])
def getemp(request):
    try:
        allemp = emp.objects.all()
        ser = empserializer(allemp,many=True)
        return Response({"data":ser.data})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})
    
@api_view(['POST'])
def addemp(request):
    try:
        ser = empserializer(data=request.data)
        if not ser.is_valid():
            return Response({"error":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"insertef data":ser.data})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})
    
@api_view(['PUT'])   
def updateemp(request,id):
    try:
        employee = emp.objects.get(pk=id)
        ser = empserializer(employee,data=request.data,partial=True)
        if not ser.is_valid():
            return Response({"error":ser.error,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"updated data":ser.data})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})
    

@api_view(['DELETE'])
def deleteemp(request,id):
    try:
        employee = emp.objects.get(pk=id)
        employee.delete()
        return Response({"deleted employee"})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})
    
class productapi(APIView):
    def get(self,request):
        try:
            allproduct = product.objects.all()
            ser = productserializer(allproduct,many=True)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"message":"something went wrong"})
        
    def post(self,request):
        try:
            ser = productserializer(data=request.data)
            if not ser.is_valid():
                return Response({"error":ser.errors,"message":"something went wrong"})
            else:
                ser.save()
                return Response({"inserted data":ser.data})
        except Exception as e:
            return Response({"message":"something went wrong"})
        
    def put(self,request):
        try:
            products = product.objects.get(pk=request.data.get('id'))
            if not products:
                return Response({"message":"Product Not Found"})
            ser = productserializer(products,request.data)
            if not ser.is_valid():
                return Response({"error":ser.errors,"message":"something went wrong"})
            ser.save()
            return Response({"updated data":ser.data})
        except Exception as e:
            return Response({"message":"something went wrong"})
        
    def delete(self,request):
        try:
            products = product.objects.get(pk=request.data.get('id'))
            if not products:
                return Response("Product Not Found")
            products.delete()
            return Response({"Product Deleted"})
        except Exception as e:
            return Response({"message":"something went wrong"})