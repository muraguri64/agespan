from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Crop_Type

# Create your views here.

def all_crops_view(request):
    crops = Crop_Type.objects
    return render(request, 'crops/all-crops.html', {'crops': crops} )


def crop_detail_view(request, crop_id):
    crop = get_object_or_404(Crop_Type, pk=crop_id)
    return render(request, 'crops/crop_detail.html', {'crop':crop})