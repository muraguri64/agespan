from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import register_Farm_Form
from .models import Register_Farm

# Create your views here.




@login_required(login_url="/accounts/login/")
def register_farm_view(request):
    form = register_Farm_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        register_farm        = form.save(commit=False)
        register_farm.user   = request.user
        register_farm.save()

        form = register_Farm_Form()
        messages.success(request, 'Farm registered successfuly!!')
        return redirect('register-farm')

    context = {
        'form': form
    }

    return render(request, 'farms/registerfarm.html', context)


def all_farms_view(request):
    farms = Register_Farm.objects
    return render(request, 'farms/allfarms.html', {'farms': farms} )


def farm_detail_view(request, farm_id):
    farm = get_object_or_404(Register_Farm, pk=farm_id)
    return render(request, 'farms/farm_detail.html', {'farm':farm})


