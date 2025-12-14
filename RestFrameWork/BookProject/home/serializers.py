from rest_framework import serializers

from .models import Books




class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"


    def validate(self, attrs):
        if attrs.get('book_name',None)is None or attrs.get('book_author',None)is None  is None or attrs.get('book_price',None) is None:
            raise serializers.ValidationError("null Value is not valid")
        return attrs

       