from django import forms

from .models import Register_Farm

class register_Farm_Form(forms.ModelForm):
    


    class Meta:
        model = Register_Farm
        exclude = ('user', 'current_problem', 'farm_history')

        widgets = {    


            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'farm_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Farm Name', 'required': True}),
            'farm_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Size of Farm', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter specific Location of the farm', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nearest Town', 'required': True}),
            'crop_grown': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'planting_date': forms.DateField(attrs={'class': 'form-control', 'required': True}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': True}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address', 'required': True}),
            'owner_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Contact Details', 'required': True}),

            'current_problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Current Problem', 'rows': 3, 'required': True}),
            'farm_history': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'FarmHistory', 'rows': 3, 'required': True}),
          

            

        }

        fields = [            
    
            'region',
            'farm_name',
            'farm_size',
            'location',
            'image',
            'nearest_town',
            'crop_grown',
            'planting_date',
            'owner_name',
            'owner_email',
            'owner_contact',
            
            'current_problem',
            'farm_history',
            'user',
        ]