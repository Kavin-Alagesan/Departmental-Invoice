from django.contrib import admin
from .models import Customermodel,Unitmodel,Productmodel,OrderDetailsmodel,Ordermodel

# Register your models here.
admin.site.register(Customermodel)
admin.site.register(Unitmodel)
admin.site.register(Productmodel)
admin.site.register(OrderDetailsmodel)
admin.site.register(Ordermodel)
