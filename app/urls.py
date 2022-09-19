from django.urls import path
from app import views

urlpatterns = [
    path('',views.create_order,name="create_order"),
    path('create/',views.create_customer_and_product,name="create_customer_and_product"),
    path('list/',views.list_order,name="list_order"),
    path('delete/<int:id>/',views.delete_order,name="delete_order"),
    path('update/<int:order_id>/',views.update_orders,name="update_order"),
    path('create_customer/',views.create_customer,name="create_customer"),
    path('list_customer/',views.list_customer,name="list_customer"),
    path('list_unit/',views.list_unit,name="list_unit"),
    path('list_product/',views.list_product,name="list_product"),
    path('update_masters/<int:id>/',views.update_masters,name="update_masters"),
    path('delete_customer/<int:customer_id>/',views.delete_customer,name="delete_customer"),
    path('delete_unit/<int:unit_id>/',views.delete_unit,name="delete_unit"),

    path('create_product/',views.create_product,name="create_product"),
    # path('list_product/',views.list_product,name="list_product"),
    path('create_unit/',views.create_unit,name="create_unit"),
    # path('list_unit/',views.list_unit,name="list_unit"),
]
