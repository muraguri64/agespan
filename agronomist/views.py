from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import register_Agronomist_Form
from .models import Register_Agronomist

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

def all_agronomists_view(request):
    agronomists = Register_Agronomist.objects
    return render(request, 'agronomist/allagronomists.html', {'agronomists': agronomists} )





