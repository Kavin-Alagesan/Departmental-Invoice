from django.db import models
from phone_field import PhoneField
from django.utils import timezone

# Create your models here.
class Customermodel(models.Model):
    customer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone_number=PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return f"{self.name} : {self.address}"

class Unitmodel(models.Model):
    unit_id=models.AutoField(primary_key=True)
    unit_name=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.unit_name}"
        
class Productmodel(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    unit_id=models.ForeignKey(Unitmodel,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name} : {self.price}"

class Ordermodel(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_no=models.CharField(max_length=30)
    order_date=models.CharField(max_length=30)
    customer_id=models.ForeignKey(Customermodel,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,null=True,blank=True)
    gross_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return self.order_no

class OrderDetailsmodel(models.Model):
    order_details_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Ordermodel,on_delete=models.CASCADE)
    get_product=models.CharField(max_length=50)
    get_unit=models.CharField(max_length=50)
    get_product_total=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    get_quantity=models.PositiveIntegerField(default=1)
    get_total_product_price=models.DecimalField(max_digits=20,decimal_places=2,default=0)
 
    def __str__(self):
        return f"{self.order_details_id} : {self.gross_amount}"
