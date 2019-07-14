from django.shortcuts import render, redirect, get_object_or_404
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


def let_equipment_detail_view(request, equipment_id):
    let_equipment = get_object_or_404(Let_Equipment, pk=equipment_id)
    return render(request, 'equipment/let_equipment_detail.html', {'let_equipment':let_equipment})

def sell_equipment_detail_view(request, equipment_id):
    sell_equipment = get_object_or_404(Sell_Equipment, pk=equipment_id)
    return render(request, 'equipment/sell_equipment_detail.html', {'sell_equipment':sell_equipment})


def all_sell_equipments_view(request):
    sell_equipments = Sell_Equipment.objects
    return render(request, 'equipment/all-sell-equipments.html', {'sell_equipments': sell_equipments} )