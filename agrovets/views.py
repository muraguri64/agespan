from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import register_Agrovet_Form, request_Product_Form
from .models import Register_Agrovet, Request_Product

# Create your views here.




@login_required(login_url="/accounts/login/")
def register_agrovet_view(request):  

    form = register_Agrovet_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        register_agrovet        = form.save(commit=False)
        register_agrovet.user   = request.user
        register_agrovet.save()

        form = register_Agrovet_Form()
        messages.success(request, 'Agrovet registered successfuly!!')
        return redirect('register-agrovet')

    context = {
        'form': form
    }

    return render(request, 'agrovets/registeragrovet.html', context) 

@login_required(login_url="/accounts/login/")
def request_product_view(request):  

    form = request_Product_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        request_product        = form.save(commit=False)
        request_product.user   = request.user
        request_product.save()

        form = register_Agrovet_Form()
        messages.success(request, 'Product requested successfuly!!')
        return redirect('request-product')

    context = {
        'form': form
    }

    return render(request, 'agrovets/requestproduct.html', context) 


def all_agrovets_view(request):
    agrovets = Register_Agrovet.objects
    return render(request, 'agrovets/allagrovets.html', {'agrovets': agrovets} )

def agrovet_detail_view(request, agrovet_id):
    agrovet = get_object_or_404(Register_Agrovet, pk=agrovet_id)
    return render(request, 'agrovets/agrovet_detail.html', {'agrovet':agrovet})


def all_requested_products_view(request):
    requested_products = Request_Product.objects
    return render(request, 'agrovets/requestedproducts.html', {'requested_products': requested_products} )



