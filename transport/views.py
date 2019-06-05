from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import request_Transport_Form, offer_Transport_Form
from .models import Request_Transport, Offer_Transport

# Create your views here.



@login_required(login_url="/accounts/login/")
def request_transport_view(request):  

    form = request_Transport_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        request_transport        = form.save(commit=False)
        request_transport.user   = request.user
        request_transport.save()

        form = request_Transport_Form()
        messages.success(request, 'Request Submitted successfuly!!')
        return redirect('request-transport')

    context = {
        'form': form
    }

    return render(request, 'transport/request-transport.html', context) 


@login_required(login_url="/accounts/login/")
def offer_transport_view(request):  

    form = offer_Transport_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        offer_transport          = form.save(commit=False)
        offer_transport.user     = request.user
        offer_transport.save()

        form = offer_Transport_Form()
        messages.success(request, 'Offer submitted successfuly!!')
        return redirect('offer-transport')

    context = {
        'form': form
    }

    return render(request, 'transport/offer-transport.html', context) 



def all_transport_requests_view(request):
    transport_requests = Request_Transport.objects
    return render(request, 'transport/transport-requests.html', {'transport_requests': transport_requests} )


def all_transport_offers_view(request):
    transport_offers = Offer_Transport.objects
    return render(request, 'transport/transport-offers.html', {'transport_offers': transport_offers} )


def transport_request_detail_view(request, request_id):
    transport_request = get_object_or_404(Request_Transport, pk=request_id)
    return render(request, 'transport/transport_request_detail.html', {'transport_request':transport_request})


def transport_offer_detail_view(request, offer_id):
    transport_offer = get_object_or_404(Offer_Transport, pk=offer_id)
    return render(request, 'transport/transport_offer_detail.html', {'transport_offer':transport_offer})





