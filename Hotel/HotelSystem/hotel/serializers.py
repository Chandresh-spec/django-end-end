from rest_framework.response import Response
from rest_framework import serializers
from .models import CustomerInfo
from django.contrib.auth.models import User



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerInfo
        fields="__all__"



class RegistrationSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    email=serializers.EmailField()




    def create(self, validated_data):
        username=validated_data["username"]
        email=validated_data["email"]

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("user already exists")
        
        user=User.objects.create(username=username,email=email)
        user.set_password(validated_data["password"])

        user.save()
        return user


class loginserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    
    

        
        
        
        
        
        