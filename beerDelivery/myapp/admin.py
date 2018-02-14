from django.contrib import admin
from .models import Beer, Store, Order, Person, Trip


admin.site.register(Beer)
admin.site.register(Person)
admin.site.register(Store)
admin.site.register(Trip)
admin.site.register(Order)
# Register your models here.
