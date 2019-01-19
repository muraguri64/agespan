from django import forms

from .models import Event

class post_Event_Form(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ('user',)

        widgets = {   

            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description', 'rows': 3, 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Location', 'required': True}),
            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nearest Town', 'required': True}),

            'start_date': forms.DateTimeInput(format='%Y-%m-%d %HH:%MM', attrs={'class': 'form-control', 'placeholder': 'YY-MM-DD Hr:Min', 'required': True}),
            'end_date': forms.DateTimeInput(format='%Y-%m-%d %HH:%MM', attrs={'class': 'form-control', 'placeholder': 'YY-MM-DD Hr:Min', 'required': True}),
            
            'organizer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organizer Name', 'required': True}),
            'organizer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Organizer Email Address', 'required': True}),
            'organizer_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organizer Contact Details', 'required': True}),
                               

        }

        fields = [    
            
            'event_name',
            'description',
            'location',
            'region',
            'nearest_town',
            'start_date',
            'end_date',
            'poster',            
            'organizer_name',
            'organizer_email',
            'organizer_contact',
            'user',
        ]
