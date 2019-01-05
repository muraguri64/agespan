from django import forms

from .models import Request_Transport, Offer_Transport

class request_Transport_Form(forms.ModelForm):

    class Meta:
        model = Request_Transport
        exclude = ('user',)

        widgets = {   

            'cargo_type': forms.Select(attrs={'class': 'form-control', 'required': True}), 
            'quantity_in_tones': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'means_of_transport': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter preferred means of transport', 'required': True}),
            'start_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter start Location', 'required': True}),
            'end_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter end Location', 'required': True}),
            'charges_per_km': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'requestor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requestor Name', 'required': True}),
            'requestor_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Requestor Email Address', 'required': True}),
            'requestor_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requestor Contact Details', 'required': True}),
                               

        }

        fields = [            
    
            'cargo_type',
            'quantity_in_tones',
            'means_of_transport',
            'start_location',
            'end_location',
            'charges_per_km',
            'requestor_name',
            'requestor_email',
            'requestor_contact',
            'user',
        ]


class offer_Transport_Form(forms.ModelForm):    


    class Meta:
        model = Offer_Transport
        exclude = ('user',)

        widgets = {   

            'vehicle_number_plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Number Plate', 'required': True}),
            'vehicle_make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Make', 'required': True}), 
            'preferred_cargo': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'charges_per_km': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),

            'offeror_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offeror Name', 'required': True}),
            'offeror_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Offeror Email Address', 'required': True}),
            'offeror_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offeror Contact Details', 'required': True}),
           
                     
        }

        fields = [            
            
            'vehicle_number_plate',
            'vehicle_make',
            'vehicle_image',
            'preferred_cargo',
            'charges_per_km',
            'offeror_name',
            'offeror_email',
            'offeror_contact',
            'user',
        ]