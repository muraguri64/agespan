from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Crop_Type

# Create your views here.

def all_crops_view(request):
    crops = Crop_Type.objects
    return render(request, 'crops/all-crops.html', {'crops': crops} )