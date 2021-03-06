from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import register_Agronomist_Form, request_Agronomist_Form
from .models import Register_Agronomist, Request_Agronomist

# Create your views here.




@login_required(login_url="/accounts/login/")
def register_agronomist_view(request):  

    form = register_Agronomist_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        register_agronomist        = form.save(commit=False)
        register_agronomist.user   = request.user
        register_agronomist.save()

        form = register_Agronomist_Form()
        messages.success(request, 'Agronomist registered successfuly!!')
        return redirect('register-agronomist')

    context = {
        'form': form
    }

    return render(request, 'agronomist/registeragronomist.html', context) 


@login_required(login_url="/accounts/login/")
def request_agronomist_view(request):  

    form = request_Agronomist_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        request_agronomist           = form.save(commit=False)
        request_agronomist.user      = request.user
        request_agronomist.save()

        form = register_Agronomist_Form()
        messages.success(request, 'Agronomist requested successfuly!!')
        return redirect('request-agronomist')

    context = {
        'form': form
    }

    return render(request, 'agronomist/requestagronomist.html', context) 



def all_agronomists_view(request):
    agronomists = Register_Agronomist.objects
    return render(request, 'agronomist/allagronomists.html', {'agronomists': agronomists} )


def agronomist_detail_view(request, agronomist_id):
    agronomist = get_object_or_404(Register_Agronomist, pk=agronomist_id)
    return render(request, 'agronomist/agronomist_detail.html', {'agronomist':agronomist})


def all_requested_agronomists_view(request):
    requested_agronomists = Request_Agronomist.objects
    return render(request, 'agronomist/requestedagronomists.html', {'requested_agronomists': requested_agronomists} )


def requested_agronomist_detail_view(request, request_id):
    requested_agronomist = get_object_or_404(Request_Agronomist, pk=request_id)
    return render(request, 'agronomist/requested_agronomist_detail.html', {'requested_agronomist':requested_agronomist})

