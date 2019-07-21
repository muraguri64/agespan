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
    market = get_object_or_404(Market, pk=market_id)
    graph_data  = market.graph_data_set

    return render(request, 'market/detail.html', {'graph_data': graph_data, 'market': market})