from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import post_Event_Form
from .models import Event
from datetime import date

# Create your views here.


@login_required(login_url="/accounts/login/")
def post_event_view(request):  

    form = post_Event_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        event          = form.save(commit=False)
        event.user     = request.user
        event.save()

        form = post_Event_Form()
        messages.success(request, 'Event submitted successfully!!')
        return redirect('post-event')

    context = {
        'form': form
    }

    return render(request, 'events/post-event.html', context) 


def upcoming_events_view(request):
    today = date.today()
    upcoming_events = Event.objects.filter(start_date__year__gte  = today.year,
                                           start_date__month__gte = today.month,
                                           start_date__day__gte   = today.day)

    return render(request, 'events/upcoming-events.html', {'upcoming_events': upcoming_events} )

def previous_events_view(request):
    today = date.today()
    previous_events = Event.objects.filter(start_date__year__lte  = today.year,
                                           start_date__month__lte = today.month,
                                           start_date__day__lte   = today.day)

    return render(request, 'events/previous-events.html', {'previous_events': previous_events} )



