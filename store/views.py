from django.shortcuts import render
from django.http import HttpResponse

from .forms import sell_Product_Form
from .models import Store_Product, Order
from django.contrib import messages

# Create your views here.

def sell_product_view(request):
    form = sell_Product_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = sell_Product_Form()
        messages.success(request, 'Product submitted successfuly')

    context = {
        'form': form
    }

    return render(request, 'store/sellproduct.html', context)
