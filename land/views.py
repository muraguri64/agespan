from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import let_Land_Form, lease_Let_Land_Form, request_To_Lease_Form, request_To_Lease_Offer_Form
from .models import Let_Land, Lease_Let_Land, Request_To_Lease, Request_To_Lease_Offer


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


def all_let_lands_view(request):
    let_lands = Let_Land.objects
    return render(request, 'land/all-let-lands.html', {'let_lands': let_lands} )