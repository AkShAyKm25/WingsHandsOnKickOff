from django.urls import path
from .views import owner, room, hotel, rooms

urlpatterns = [
    path('owner/', owner.as_view()),
    path('hotel/', hotel.as_view()),
    path('room/', rooms.as_view()),
    path('room/<int:pk>', room.as_view())
]
