from django import forms

from .models import Register_Agrovet, Request_Product

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


class request_Product_Form(forms.ModelForm):
    


    class Meta:
        model = Request_Product
        exclude = ('user',)

        widgets = {    

            'requestor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requestor Name', 'required': True}),
            'requestor_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Requestor Email Address', 'required': True}),
            'requestor_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requestor Contact Details', 'required': True}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name', 'required': True}),
            
            'farm_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Farm Name', 'required': True}),
            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'delivery_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter delivery Location', 'required': True}),
            'product_purpose': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Product Purpose', 'rows': 3, 'required': True}),
           
                    

        }

        fields = [            
    
            'requestor_name',
            'requestor_email',
            'requestor_contact',
            'product_name',
            'farm_name',
            'region',           
            'delivery_location',            
            'product_purpose',
            'user',
        ]