from distutils.sysconfig import customize_compiler
from rest_framework import serializers
from .models import Customermodel,Unitmodel,Productmodel,OrderDetailsmodel,Ordermodel

# Create Customer and Unit
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customermodel
        fields=['customer_id','name','address','phone_number']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Unitmodel
        fields=['unit_id','unit_name']

# Nested serializers
class ProductNestedSerializer(serializers.ModelSerializer):
    unit_id=UnitSerializer()
    class Meta:
        model=Productmodel
        fields=['product_id','product_name','unit_id','price']

class OrderNestedSerializer(serializers.ModelSerializer):
    customer_id=CustomerSerializer()
    class Meta:
        model=Ordermodel
        fields=['order_id','order_no','order_date','customer_id','description','gross_amount']

class OrderDetailsNestedSerializer(serializers.ModelSerializer):
    order_id=OrderNestedSerializer()
    class Meta:
        model=OrderDetailsmodel
        fields=['order_details_id','order_id','get_product','get_unit','get_product_total','get_quantity','get_total_product_price']

# Nested to list details inside order number
class ListOrderDetailsSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    # customer=serializers.SerializerMethodField()
    customer_id =CustomerSerializer()

    class Meta:
        model = Ordermodel
        fields = ['order_id','order_no','customer_id' ,'order_date','gross_amount','description','details']

    def get_details(self, obj):
        data = OrderDetailsmodel.objects.filter(order_id=obj.order_id).values()
        return data

    # def get_customer(self, obj):
    #     data = Customermodel.objects.filter(name=obj.customer_id).values()
    #     return data

# Nonnested serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productmodel
        fields=['product_id','product_name','unit_id','price']

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetailsmodel
        fields=['order_details_id','order_id','get_product','get_unit','get_product_total','get_quantity','get_total_product_price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ordermodel
        fields=['order_id','order_no','order_date','customer_id', 'description','gross_amount']

class OrderCountSerializer(serializers.ModelSerializer):
    order_no = serializers.SerializerMethodField()
    class Meta:
        model = Ordermodel
        fields = ['order_id','order_no']

    def get_order_no(self, obj):
        try:
            data = Ordermodel.objects.last()
            values =data.order_id + 1
            return "OR%0004d" % values
        except:
            return "OR0001"
