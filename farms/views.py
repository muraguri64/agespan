from django.shortcuts import render, redirect
from django.http import HttpResponse
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

