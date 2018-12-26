from django import forms

from .models import Register_Agrovet

class register_Agrovet_Form(forms.ModelForm):
    


    class Meta:
        model = Register_Agrovet
        exclude = ('user',)

        widgets = {    

            'agrovet_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agrovet Name', 'required': True}),
            'agrovet_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Agrovet Email Address', 'required': True}),
            'agrovet_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agrovet Contact Details', 'required': True}),

            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter specific Location of the farm', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nearest Town', 'required': True}),
           
                    

        }

        fields = [            
    
            'agrovet_name',
            'agrovet_email',
            'agrovet_contact',
            'region',           
            'location',            
            'nearest_town',
            'user',
        ]