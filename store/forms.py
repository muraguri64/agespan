from django import forms

from .models import Store_Product

class sell_Product_Form(forms.ModelForm):
    


    class Meta:
        model = Store_Product

        widgets = {
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': True}),
            'seller_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address', 'required': True}),
            'seller_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Contact Details', 'required': True}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'crop_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location of Nearest Town', 'required': True}),
            'farm_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Size of Farm', 'required': True}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'units': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3, 'required': True}),
         

            



            

            

        }

        fields = [
            'seller_name',
            'seller_email',
            'seller_contact',
            'product_name',
            'crop_type',
            'region',
            'nearest_town',
            'farm_size',
            'quantity',
            'units',
            'unit_price',
            'image',
            'description',
        ]