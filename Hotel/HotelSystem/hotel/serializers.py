from rest_framework.response import Response
from rest_framework import serializers
from .models import CustomerInfo



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerInfo
        fields="__all__"

