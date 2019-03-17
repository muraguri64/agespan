from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Market

# Create your views here.

def market_view(request):

    markets = Market.objects
    return render(request, 'market/market.html', {'markets': markets})



def market_detail_view(request, market_id):
    market_detail = get_object_or_404(Market, pk=market_id)
    return render(request, 'market/detail.html', {'market_detail': market_detail})