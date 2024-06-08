from django.contrib import admin
from .models import OwnerModel, HotelModel, RoomModel

# Register your models here.
admin.site.register(OwnerModel)
admin.site.register(HotelModel)
admin.site.register(RoomModel)
