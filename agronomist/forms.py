from django import forms

from .models import Register_Agronomist, Request_Agronomist

class register_Agronomist_Form(forms.ModelForm):
    


    class Meta:
        model = Register_Agronomist
        exclude = ('user',)

        widgets = {    

            'agronomist_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agronomist Name', 'required': True}),
            'agronomist_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Agronomist Email Address', 'required': True}),
            'agronomist_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agronomist Contact Details', 'required': True}),

            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'crop_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'profile': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Agronomist Profile/Achievement', 'rows': 3, 'required': True}),
            'advice': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Agronomist Contribution/Advice', 'rows': 3, 'required': True}),
           
                    

        }

        fields = [            
    
            'agronomist_name',
            'agronomist_email',
            'agronomist_contact',
            'region',           
            'crop_type',            
            'profile',
            'advice',
            'user',
        ]

