from django.shortcuts import render,redirect
from django.conf import settings
import requests
from django.contrib import messages
import json
from django.db import transaction

from django.http import HttpResponse

url=settings.URL

# Create your views here.
def create_customer_and_product(request):
    unit_data=requests.get('{url}unit/'.format(url=url)).json()        
    return render(request,'order_manage/create_customer_and_product.html',{'unit_data':unit_data})

def list_order(request):
    print('-------------------------list order-------------')
    order_data=requests.get('{url}order_nested/'.format(url=url)).json()
    return render(request,"order_manage/list_order.html",{'order_data':order_data})

def create_order(request):
    if request.method=='POST':
        print('------------post-------------')
        order_no=request.POST['txtOrderNo']
        order_date=request.POST['txtOrderDate']
        customer=request.POST['ddlCustomer']
        description=request.POST['txtDescription']
        total_amount=request.POST['txtTotalAmt']
        
        data={
            'order_no':order_no,
            'order_date':order_date,
            'customer_id':customer,
            'description':description,
            'gross_amount':total_amount,
            }
        
        # response=requests.post('{url}order/'.format(url=url), data=data)
        # print('------------postdata-------------')
        try:
            hiddenData = request.POST['hiddenData']
            data_json=json.loads(hiddenData)
            print(data_json)
            print(type(data_json))
            
            with transaction.atomic():
                response=requests.post('{url}order/'.format(url=url), data=data)
                print('------------postdata1-------------')

                value =response.text
                print('------------endpostdata-------------')
                json_value=json.loads(value)
                get_order_id=json_value['order_id']

            # value =response.text
            # print('------------endpostdata-------------')
            # json_value=json.loads(value)
            # get_order_id=json_value['order_id']

            for return_data in data_json:
                hidden_product=return_data['get_product']
                hidden_unit=return_data['get_unit']
                hidden_price=return_data['get_product_total']
                hidden_quantity=return_data['get_quantity']
                hidden_total_amount=return_data['get_total_product_price']

                table_data={
                    'order_id':get_order_id,
                    'get_product':hidden_product,
                    'get_unit':hidden_unit,
                    'get_product_total':hidden_price,
                    'get_quantity':hidden_quantity,
                    'get_total_product_price':hidden_total_amount,
                }

                table_response=requests.post('{url}order_details/'.format(url=url), data=table_data)
                print(table_response)
                print('------------postdata2-------------')
            
            messages.success(request,("Order data entered successfully"))
            return redirect('list_order')
        except:
            messages.error(request,("Data entered failed"))
            return redirect('create_order')

    else:
        print('-------------------------else-------------')
        customer_data=requests.get('{url}customer/'.format(url=url)).json()
        product_data=requests.get('{url}product_nested/'.format(url=url)).json()
        return render(request,"order_manage/create_order.html",{'customer_data':customer_data,'product_data':product_data})


def update_orders(request,order_id):
    if request.POST.get('btnSaveorder','') == 'SaveOrder':
        name =  request.POST['ddlCustomer']
        order_no =  request.POST['txtOrderNo']
        ord_date = request.POST['txtOrderDate']
        total_amount = request.POST['txtTotalAmt']
        product_desc = request.POST['txtDescription']
        data = {
            'customer_id': name,
            'order_no': order_no,
            'order_date': ord_date,
            'gross_amount' : total_amount,
            'description' : product_desc
            }
        response = requests.put('{url}order/{pk}/'.format(pk=order_id,url=url),data=data)
        print(response.text)
        return redirect('create_order')
    
    elif request.POST.get('btnHiddenEditValue','') == 'EditOrder':
        if_value = request.POST['btnHiddenEditValue']
        print("check:",if_value)
        order_list = requests.get('{url}listupdate/{pk}/'.format(url=url,pk=order_id)).json()
        product_data = requests.get('{url}product_nested/'.format(url=url)).json()
        print("---------order_list--------------")
        print(order_list)
        print(product_data)
        return render(request,'order_manage/create_order.html',{'order_list' : order_list,'if_value' : if_value,'product_data' :product_data})

    else:
        print("-------redirect---------")
        return render(request,'order_manage/create_order.html')

def delete_order(request,id):
    response=requests.delete("{url}order/{pk}/".format(url=url, pk=id))
    messages.success(request,("Order deleted successfully"))
    return redirect('list_order')

def create_customer(request):
    if request.method=='POST':
        name=request.POST['txtCustomerName']
        address=request.POST['txtCustomerAddress']
        phone_number=request.POST['txtPhoneNo']
        print('------------customer-------------')
        data={
            'name':name,
            'address':address,
            'phone_number':phone_number,
            }
        response=requests.post('{url}customer/'.format(url=url), data=data)
        print(data)
        print(response.text)
        messages.success(request,("customer data entered successfully"))
        return redirect('create_customer_and_product')
    else:
        print('-------------------------else customer-------------')
        unit_data=requests.get('{url}unit/'.format(url=url)).json()
        return render(request,'order_manage/create_customer_and_product.html',{'unit_data':unit_data})
        # return render(request,'order_manage/edit_customer.html',{'unit_data':unit_data})
        
def create_product(request):
    if request.method=='POST':
        product_name=request.POST['txtProductName']
        price=request.POST['txtProductPrice']
        unit_id=request.POST['ddlUnit']
        print('------------product-------------')
        data={
            'product_name':product_name,
            'unit_id':unit_id,
            'price':price,
            }
        response=requests.post('{url}product/'.format(url=url), data=data)
        print(data)
        print(response.text)
        messages.success(request,("Product data entered successfully"))
        return redirect('create_customer_and_product')
    else:
        print('-------------------------product else-------------')
        unit_data=requests.get('{url}unit/'.format(url=url)).json()        
        return render(request,'order_manage/create_customer_and_product.html',{'unit_data':unit_data})

def create_unit(request):
    if request.method=='POST':
        unit=request.POST['txtUnit']
        print('------------unit-------------')
        data={
            'unit_name':unit,
            }
        response=requests.post('{url}unit/'.format(url=url), data=data)
        print(data)
        print(response.text)
        messages.success(request,("Unit entered successfully"))
        return redirect('create_customer_and_product')
    else:
        print('-------------------------unit else-------------')
        unit_data=requests.get('{url}unit/'.format(url=url)).json()        
        return render(request,'order_manage/create_customer_and_product.html',{'unit_data':unit_data})

def update_masters(request,id):
    if request.POST.get('hiddenCustomerVal','') == 'UpdateCustomer':
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')      
        name =  request.POST['txtCustomerName']
        address =  request.POST['txtCustomerAddress']
        phone_number = request.POST['txtPhoneNo']
        data = {
            'name': name,
            'address': address,
            'phone_number': phone_number,
            }
        print('------------------update customer------------------------')
        print(data)
        response = requests.put('{url}customer/{pk}/'.format(pk=id,url=url),data=data)
        print(response.text)
        messages.success(request,("customer data updated successfully"))
        return redirect('list_customer')

    elif request.POST.get('hiddenUnitVal','') == 'UpdateUnit':
        unit_name =  request.POST['txtUnitName']
        data = {
            'unit_name': unit_name,
            }
        print('--------------------update unit------------------------')
        print(data)
        response = requests.put('{url}unit/{pk}/'.format(pk=id,url=url),data=data)
        print(response.text)
        messages.success(request,("Unit data updated successfully"))
        return redirect('list_unit')

    elif request.POST.get('hiddenProductVal','') == 'UpdateProduct':
        product_name =  request.POST['txtProductName']
        unit_name =  request.POST['txtUnitName']
        price =  request.POST['txtPrice']
        data = {
            'unit_name': unit_name,
            }
        print('--------------------update unit------------------------')
        print(data)
        response = requests.put('{url}unit/{pk}/'.format(pk=id,url=url),data=data)
        print(response.text)
        messages.success(request,("Unit data updated successfully"))
        return redirect('list_unit')

    # else:
    #     print('-------------------------else customer-------------')
    #     unit_data=requests.get('{url}unit/'.format(url=url)).json()
    #     return render(request,'order_manage/create_customer_and_product.html',{'unit_data':unit_data})

def list_customer(request):
    print('-------------------------list customer-------------')
    order_data=requests.get('{url}customer/'.format(url=url)).json()
    print(order_data)
    return render(request,"order_manage/edit_customer.html",{'order_data':order_data})

def list_unit(request):
    print('-------------------------list customer-------------')
    order_data=requests.get('{url}unit/'.format(url=url)).json()
    print(order_data)
    return render(request,"order_manage/edit_unit.html",{'order_data':order_data})

def list_product(request):
    print('-------------------------list product-------------')
    order_data=requests.get('{url}product_nested/'.format(url=url)).json()
    print(order_data)
    return render(request,"order_manage/edit_product.html",{'order_data':order_data})

def delete_customer(request,customer_id):
    response=requests.delete("{url}customer/{pk}/".format(pk=customer_id,url=url))
    messages.success(request,("Customer deleted successfully"))
    return redirect('list_customer')

def delete_unit(request,unit_id):
    response=requests.delete("{url}unit/{pk}/".format(pk=unit_id,url=url))
    messages.success(request,("Unit deleted successfully"))
    return redirect('list_unit')

def delete_product(request,product_id):
    response=requests.delete("{url}product_nested/{pk}/".format(pk=product_id,url=url))
    messages.success(request,("Product deleted successfully"))
    return redirect('list_product')

# def list_product(request):
#     print('-------------------------list product-------------')
#     order_data=requests.get('{url}order_nested/'.format(url=url)).json()
#     return render(request,"order_manage/list_order.html",{'order_data':order_data})

# def list_unit(request):
#     print('-------------------------list unit-------------')
#     order_data=requests.get('{url}order_nested/'.format(url=url)).json()
#     return render(request,"order_manage/list_order.html",{'order_data':order_data})

