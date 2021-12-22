from django.shortcuts import render, redirect
from django.views import View
from dashboard.models import Product
from dashboard.forms import ProductForm
from django.http import HttpResponse
from django.views.generic import CreateView
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

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'price', 'category')
    template_name = "dashboard/form.html"

def displayProductDetails(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        context = {}

        context['product'] = product
        return render(request, "dashboard/product_details.html", context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form,
        'product': product
    }
    return render(request, 'dashboard/form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
       product.delete()
       return redirect('/')
    
    context = {
        'product': product
    }
    return render(request, 'dashboard/delete.html', context)


