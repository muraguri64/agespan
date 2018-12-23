from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import sell_Product_Form
from .models import Store_Product, Order


# Create your views here.

@login_required(login_url="/accounts/login/")
def sell_product_view(request):
    form = sell_Product_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        sellproduct = form.save(commit=False)
        sellproduct.user = request.user
        sellproduct.save()

        form = sell_Product_Form()
        messages.success(request, 'Product submitted successfuly!!')
        return redirect('sellproduct')

    context = {
        'form': form
    }

    return render(request, 'store/sellproduct.html', context)


def store_products_view(request):
    products = Store_Product.objects
    return render(request, 'store/storeproducts.html', {'products': products} )
