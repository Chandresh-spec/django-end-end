from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import CustomerInfo
from .serializers import CustomerSerializer,RegistrationSerializer,loginserializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class customer(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        items=CustomerInfo.objects.all()
        paginator=PageNumberPagination()
        paginator.page_size=3
        paginator_items=paginator.paginate_queryset(items,request)
        serializer=CustomerSerializer(paginator_items,many=True)
        return  paginator.get_paginated_response(serializer.data)
    

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

            if  not user:
              return Response({
                "status":False,
                "message":"validation Failed"
            },status=status.HTTP_400_BAD_REQUEST)
            token, _ = Token.objects.get_or_create(user=user)  
            return Response({
                "status":False,
                "message":"user not found",
                "error":serializer.errors,
                "Token":token.key
            },status=status.HTTP_400_BAD_REQUEST)
        

        return Response(
            {
                "status":False,
                "errors":serializer.errors,
                "message":"validation failed"
            }
        )



def home(request):
    return render(request,'index.html')