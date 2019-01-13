from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import let_Equipment_Form,sell_Equipment_Form
from .models import Let_Equipment, Sell_Equipment

# Create your views here.


@login_required(login_url="/accounts/login/")
def let_equipment_view(request):  

    form = let_Equipment_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        let_equipment        = form.save(commit=False)
        let_equipment.user   = request.user
        let_equipment.save()

        form = let_Equipment_Form()
        messages.success(request, 'Equipment Submitted successfully!!')
        return redirect('let-equipment')

    context = {
        'form': form
    }

    return render(request, 'equipment/let-equipment.html', context) 


@login_required(login_url="/accounts/login/")
def sell_equipment_view(request):  

    form = sell_Equipment_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        sell_equipment          = form.save(commit=False)
        sell_equipment.user     = request.user
        sell_equipment.save()

        form = sell_Equipment_Form()
        messages.success(request, 'Equipment submitted successfully!!')
        return redirect('sell-equipment')

    context = {
        'form': form
    }

    return render(request, 'equipment/sell-equipment.html', context) 


def all_let_equipments_view(request):
    let_equipments = Let_Equipment.objects
    return render(request, 'equipment/all-let-equipments.html', {'let_equipments': let_equipments} )


def all_sell_equipments_view(request):
    sell_equipments = Sell_Equipment.objects
    return render(request, 'equipment/all-sell-equipments.html', {'sell_equipments': sell_equipments} )