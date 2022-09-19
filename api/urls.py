from django.urls import path
from api.views import CustomerListCreateAPI,UnitListCreateAPI,ProductListCreateAPI,OrderDetailsListCreateAPI,OrderListCreateAPI,ProductListNestedAPI,OrderDetailsNestedAPI,OrderListNestedAPI,ProductWithIDNestedAPI,OrderUpdateDelete,OrderListIDNestedAPI,OrderCount,List,ListUpdateDelete,CustomerUpdateDelete,UnitUpdateDelete

urlpatterns = [
    path('customer/',CustomerListCreateAPI.as_view()),
    path('customer/<int:pk>/',CustomerUpdateDelete.as_view()),
    path('unit/',UnitListCreateAPI.as_view()),
    path('unit/<int:pk>/',UnitUpdateDelete.as_view()),
    path('product_nested/',ProductListNestedAPI.as_view()),
    path('product/',ProductListCreateAPI.as_view()),
    path('product_nested/<int:pk>/',ProductWithIDNestedAPI.as_view()),
    # path('api_region/<int:pk>/',RegionUpdateDelete.as_view()),
    path('order_details_nested/',OrderDetailsNestedAPI.as_view()),
    path('order_details/',OrderDetailsListCreateAPI.as_view()),
    # path('api_region/<int:pk>/',RegionUpdateDelete.as_view()),
    path('order_nested/',OrderListNestedAPI.as_view()),
    path('order_nested/<int:pk>/',OrderListIDNestedAPI.as_view()),
    path('order/',OrderListCreateAPI.as_view()),
    path('order/<int:pk>/',OrderUpdateDelete.as_view()),
    path('order_no/', OrderCount.as_view()),
    path('list/',List.as_view()),
    path('listupdate/<int:pk>/',ListUpdateDelete.as_view())
    ]

    
