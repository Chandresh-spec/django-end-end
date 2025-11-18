from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import CustomerInfo
from .serializers import CustomerSerializer,RegistrationSerializer,loginserializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
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
    def put(self,request):
        id=self.request.GET.get('id')
        st=get_object_or_404(CustomerInfo,id=id)
        serializer=CustomerSerializer(st,data=request.data)
        # print(serializer.data)
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
    def patch(self,request):
        id=self.request.GET.get("id")
        st=get_object_or_404(CustomerInfo,id=id)

        serializer=CustomerSerializer(st,data=request.data,partial=True)
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
     

    def delete(self,request):
        id=self.request.GET.get("id")
        st=get_object_or_404(CustomerInfo,id=id)

        if st:
            st.delete()
            return Response({
                "status":True,
                "message":"object deleted"
            },status=status.HTTP_200_OK)
        
        return Response(
            {
                "status":False,
                "message":"object not found"
            },status=status.HTTP_400_BAD_REQUEST
        )
        
        
    
        
        
        
class RegistrationViews(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "status":False,
                    "message":"validation  fails",
                    "erros":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            {
                "status":True,
                "message":"user created",
            },status=status.HTTP_200_OK
        )
    




class Login_View(APIView):
    def post(self,request):

        serializer=loginserializer(data=request.data)

        if serializer.is_valid():
            username=serializer.validated_data["username"]
            password=serializer.validated_data["password"]

            user=authenticate(username=username,password=password)

            if user:
              return Response({
                "status":True,
                "message":"user logged in"
            },status=status.HTTP_200_OK)
        return Response({
            "status":False,
            "message":"user not found",
            "error":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)


    