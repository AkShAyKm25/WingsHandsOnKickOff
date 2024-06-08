from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RoomModel, OwnerModel, HotelModel
from .serializers import RoomModelSerializer, OwnerModelSerializer, HotelModelSerializer 

# Create your views here.
class owner(APIView):
    def post(self, request):
        serializer=OwnerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class hotel(APIView):
    def post(self, request):
        serializer=HotelModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class rooms(APIView):
    def post(self, request, pk=None):
        serializer=RoomModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class room(APIView):
    def get(self, request, pk):
        try:
            data=RoomModel.objects.get(pk=pk)
        except RoomModel.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=RoomModelSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        try:
            data=RoomModel.objects.get(pk=pk)
        except RoomModel.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer=RoomModelSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            data=RoomModel.objects.get(pk=pk)
        except RoomModel.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        


