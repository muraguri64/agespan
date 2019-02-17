from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import let_Land_Form, request_To_Lease_Form, sell_Land_Form, request_To_Buy_Form
from .models import Let_Land, Request_To_Lease, Sell_Land, Request_To_Buy


def lease_view(request):    
    return render(request, 'land/main/lease.html')

def all_lease_requests_view(request):
    lease_requests = Request_To_Lease.objects
    return render(request, 'land/all-lease-requests.html', {'lease_requests': lease_requests} )

@login_required(login_url="/accounts/login/")
def request_to_lease_view(request):  

    form = request_To_Lease_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        request_to_lease          = form.save(commit=False)
        request_to_lease.user     = request.user
        request_to_lease.save()

        form = request_To_Lease_Form()
        messages.success(request, 'Request submitted successfully!!')
        return redirect('request-to-lease')

    context = {
        'form': form
    }

    return render(request, 'land/request-to-lease.html', context) 




def let_view(request):    
    return render(request, 'land/main/let.html')

def all_let_lands_view(request):
    let_lands = Let_Land.objects
    return render(request, 'land/all-let-lands.html', {'let_lands': let_lands} )


@login_required(login_url="/accounts/login/")
def let_land_view(request):
    form = let_Land_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        let_land          = form.save(commit=False)
        let_land.user     = request.user
        let_land.save()

        form = let_Land_Form()
        messages.success(request, 'Land submitted successfully!!')
        return redirect('let-land')

    context = {
        'form': form
    }

    return render(request, 'land/let-land.html', context) 


def sell_view(request):    
    return render(request, 'land/main/sell.html')

def all_buyer_requests_view(request):
    buyer_requests = Request_To_Buy.objects
    return render(request, 'land/all-buyer-requests.html', {'buyer_requests': buyer_requests} )

@login_required(login_url="/accounts/login/")
def sell_land_view(request):
    form = sell_Land_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        sell_land          = form.save(commit=False)
        sell_land.user     = request.user
        sell_land.save()

        form = sell_Land_Form()
        messages.success(request, 'Land submitted successfully!!')
        return redirect('sell-land')

    context = {
        'form': form
    }

    return render(request, 'land/sell-land.html', context) 




def buy_view(request):    
    return render(request, 'land/main/buy.html')

def all_sell_lands_view(request):
    sell_lands = Sell_Land.objects
    return render(request, 'land/all-sell-lands.html', {'sell_lands': sell_lands} )

@login_required(login_url="/accounts/login/")
def request_to_buy_view(request):  

    form = request_To_Buy_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        request_to_buy          = form.save(commit=False)
        request_to_buy.user     = request.user
        request_to_buy.save()

        form = request_To_Buy_Form()
        messages.success(request, 'Request submitted successfully!!')
        return redirect('request-to-buy')

    context = {
        'form': form
    }

    return render(request, 'land/request-to-buy.html', context) 