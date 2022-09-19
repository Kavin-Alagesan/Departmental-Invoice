from rest_framework import generics,status
from .models import Customermodel,Unitmodel,Productmodel,OrderDetailsmodel,Ordermodel
from .serializers import CustomerSerializer,UnitSerializer,ProductNestedSerializer,OrderDetailsNestedSerializer,OrderNestedSerializer,ProductSerializer,OrderDetailsSerializer,OrderSerializer,OrderCountSerializer,ListOrderDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# Create and list
class CustomerListCreateAPI(generics.ListCreateAPIView):
    queryset=Customermodel.objects.all()
    serializer_class=CustomerSerializer

class UnitListCreateAPI(generics.ListCreateAPIView):
    queryset=Unitmodel.objects.all()
    serializer_class=UnitSerializer

# Nested serializers
class ProductListNestedAPI(generics.ListAPIView):
    queryset=Productmodel.objects.all()
    serializer_class=ProductNestedSerializer

class OrderDetailsNestedAPI(generics.ListAPIView):
    queryset=OrderDetailsmodel.objects.all()
    serializer_class=OrderDetailsNestedSerializer

class OrderListNestedAPI(generics.ListAPIView):
    queryset=Ordermodel.objects.all()
    serializer_class=OrderNestedSerializer

# Nonnested serializers
class ProductListCreateAPI(generics.ListCreateAPIView):
    queryset=Productmodel.objects.all()
    serializer_class=ProductSerializer

class OrderDetailsListCreateAPI(generics.ListCreateAPIView):
    queryset=OrderDetailsmodel.objects.all()
    serializer_class=OrderDetailsSerializer

class OrderListCreateAPI(APIView):
    def get(self,request):
        order=Ordermodel.objects.all()
        serializer=OrderSerializer(order,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Nested serializers with ID
class ProductWithIDNestedAPI(generics.RetrieveUpdateAPIView):
    queryset=Productmodel.objects.all()
    serializer_class=ProductNestedSerializer

class OrderListIDNestedAPI(generics.RetrieveUpdateAPIView):
    queryset=Ordermodel.objects.all()
    serializer_class=OrderNestedSerializer

# Update and Delete
class OrderUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ordermodel.objects.all()
    serializer_class=OrderSerializer

class CustomerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customermodel.objects.all()
    serializer_class=CustomerSerializer

class UnitUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Unitmodel.objects.all()
    serializer_class=UnitSerializer

# Order number
class OrderCount(generics.ListAPIView):
    queryset=Ordermodel.objects.all()
    serializer_class = OrderCountSerializer

# List Order Details with regards to order number
class List(generics.ListCreateAPIView):
    queryset = Ordermodel.objects.all()
    serializer_class = ListOrderDetailsSerializer

class ListUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ordermodel.objects.all()
    serializer_class = ListOrderDetailsSerializer
