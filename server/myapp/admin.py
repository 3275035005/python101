from django.contrib import admin

# Register your models here.
from myapp.models import  User, ChargingPile, ChargingStation, Banner, Order, Feedback, File


admin.site.register(User)
admin.site.register(ChargingPile)
admin.site.register(ChargingStation)
admin.site.register(Banner)
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(File)