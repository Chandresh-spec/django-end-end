from django.shortcuts import render

from rest_framework.views import APIView
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializers
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import GenericAPIView

from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.


class Boooks_views(APIView):
    
    def get(self,request):
        book=Books.objects.all()

        serializer=BookSerializers(book,many=True)

        return Response(serializer.data)
    


    def post(self,request):
        serializer=BookSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({
                "status":False,
                "message":"validation fails",
                "errors":serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            "status":True,
            "message":"validation pass",
            
        },status=status.HTTP_201_CREATED)
    


    def put(self,request):
        id=request.GET.get('id')

        book=get_object_or_404(Books,id=id)

        serilazer=BookSerializers(book,data=request.data)


        if not serilazer.is_valid():
            return Response({
                        "status":False,
                        "message":"validation fails",
                        "errors":serilazer.errors
                        },status=status.HTTP_400_BAD_REQUEST)
        
        serilazer.save()
        return Response({
                "status":True,
                "message":"validation pass",

            },status=status.HTTP_201_CREATED)
    



    def patch(self,request):
        id=request.GET.get('id')
        book=get_object_or_404(Books,id=id)
        serilazer=BookSerializers(book,data=request.data,partial=True)
        if not serilazer.is_valid():
                return Response({
                    "status":False,
                    "message":"validation fails",
                    "errors":serilazer.errors
                    },status=status.HTTP_400_BAD_REQUEST)

        serilazer.save()
        return Response({
        "status":True,
        "message":"validation pass",
        },status=status.HTTP_201_CREATED)
    


    def delete(self,request):
        id=request.GET.get('id')
        book=get_object_or_404(Books,id=id)

        book.delete()
        return Response({
            "status":"sucess"
        })





class BookMixinsView(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView

):
    queryset=Books.objects.all()
    serializer_class=BookSerializers


    def get(self,request,pk=None):
        if pk:
            return self.retrieve(request,pk=pk)

        return self.list(request)
    

    def post(self,request):
        return self.create(request,data=request.data)
    

    def put(self,request,pk):
        return self.update(request,data=request.data,pk=pk)
    

    def patch(self,request,pk):
        return self.update(request,data=request.data ,partial=True,pk=pk)
    

    def delete(self,request,pk):
        return self.destroy(request,pk=pk)




class BookViewset(ModelViewSet):
    queryset=Books.objects.all()
    serializer_class=BookSerializers


