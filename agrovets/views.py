from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.




@login_required(login_url="/accounts/login/")
def register_agrovet_view(request):   

    return HttpResponse("Register Agrovet View")



