from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomerInfo
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class customer(APIView):
    def get(self,request):
        items=CustomerInfo.objects.all()
        serializer=CustomerSerializer(items,many=True)
        return  Response(serializer.data)
    

    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                 "message":"validation Fails",
                 "error":serializer.errors
     
                 },status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save()
        return Response(
            {
                "status":True,
                "message":"sucessfull",
                
            },status=status.HTTP_200_OK
        )
    
        
        
        
        
        