from rest_framework import serializers
from .models import RoomModel, HotelModel, OwnerModel


class OwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=OwnerModel
        fields='__all__'

class HotelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelModel
        fields='__all__'

class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomModel
        fields='__all__'
