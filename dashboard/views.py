from django.shortcuts import render, redirect
from django.views import View
from dashboard.models import Product
from dashboard.forms import ProductForm
from django.http import HttpResponse
import json

class MainPage(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        form = ProductForm()
        total_hardwares = products.filter(category='Hardware').count()
        total_softwares = products.filter(category='Software').count()
        total_devices = products.filter(category='Device').count()
        total_products = products.count()

        context = {
            'products': products,
            'total_hardwares': total_hardwares,
            'total_softwares': total_softwares,
            'total_devices': total_devices,
            'total_products': total_products,
            'form': form
        }

        return render(request, "dashboard/home.html", context)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.POST.get('data'))
        response_data = {}

        prod_name = data['name']
        prod_price = data['price']
        category = data['category']

        print(data)
        product = Product(name=prod_name, price=prod_price, category=category)
        # form = ProductForm(request.POST, initial={'name': prod_name, 'price': prod_price, 'category': category})
        # form = ProductForm(request.POST)
        
        if product.name:
            product.save()
            response_data['mode'] = 'success'
            response_data['message'] = 'Product added successfully!'
            
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

        # context = {'form': form}
        response_data['mode'] = 'error'
        response_data['message'] = 'Failed to add product'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def displayProductDetails(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        context = {}

        context['product'] = product
        return render(request, "dashboard/product_details.html", context)
def updateProductAJAX(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'GET':
        product_data = {}

        product_data['name'] = product.name
        product_data['price'] = product.price
        product_data['category'] = product.category

        return HttpResponse(
            json.dumps(product_data),
            content_type="application/json"
        )
        
    else:
        data = json.loads(request.POST.get("data"))
        response_data = {}
        product.name = data['name']
        product.price = data['price']
        product.category = data['category']

        if product.name:
            product.save()
            response_data['mode'] = 'success'
            response_data['message'] = 'Product is updated successfully!'
            
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

    response_data['mode'] = 'error'
    response_data['message'] = 'Error in updating product'
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'GET':
        response_data = {}

        response_data['name'] = product.name
        response_data['price'] = product.price
        response_data['category'] = product.category

        return HttpResponse(
            json.dumps(response_data),
            content_type='application/json'
        )

    elif request.method == 'POST':
        response_data = {}
        product.delete()

        response_data['success'] = 'success'
        response_data['message'] = 'Product has been removed successfully!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def showData(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)

        response_data = {}

        response_data['name'] = product.name
        response_data['price'] = product.price
        response_data['category'] = product.category
        response_data['date_created'] = str(product.date_created.strftime("%d %B, %Y %I:%M %p"))

        print(response_data)

        return HttpResponse(
            json.dumps(response_data),
            content_type='application/json'
        )

        

    


