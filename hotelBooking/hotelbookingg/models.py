from django.db import models

# Create your models here.
class OwnerModel(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True, default="")
    password = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.id)

class HotelModel(models.Model):
    hotel_name = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    owner_id = models.ForeignKey(OwnerModel, related_name='hotels', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
class RoomModel(models.Model):
    room_no = models.CharField(max_length=50, default="")
    rent = models.FloatField(default=0.0)
    is_occupied = models.BooleanField(default=False)
    hotel_id = models.ForeignKey(HotelModel, related_name='rooms', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)