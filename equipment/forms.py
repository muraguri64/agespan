from django import forms

from .models import Let_Equipment, Sell_Equipment


class let_Equipment_Form(forms.ModelForm):

    class Meta:
        model = Let_Equipment
        exclude = ('user',)

        widgets = {   

            'equipment_type': forms.Select(attrs={'class': 'form-control', 'required': True}), 
            'equipment_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Equipment Name', 'required': True}),
            'manufacture_year': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'YY-MM-DD', 'required': True}),
            
            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'current_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Current Location', 'required': True}),
            'price_per': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Name', 'required': True}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Owner Email Address', 'required': True}),
            'owner_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Contact Details', 'required': True}),
                               

        }

        fields = [            
    
            'equipment_type',
            'equipment_name',
            'manufacture_year',
            'region',
            'current_location',
            'image',
            'price_per',
            'price',
            'owner_name',
            'owner_email',
            'owner_contact',
            'user',
        ]


class sell_Equipment_Form(forms.ModelForm):

    class Meta:
        model = Sell_Equipment
        exclude = ('user',)

        widgets = {   

            'equipment_type': forms.Select(attrs={'class': 'form-control', 'required': True}), 
            'equipment_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Equipment Name', 'required': True}),
            'manufacture_year': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'YY-MM-DD', 'required': True}),
            
            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'current_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Current Location', 'required': True}),
            'price_range_from': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price Range From', 'required': True}),
            'price_range_to': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price Range To', 'required': True}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Name', 'required': True}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Owner Email Address', 'required': True}),
            'owner_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Contact Details', 'required': True}),
                               

        }

        fields = [            
    
            'equipment_type',
            'equipment_name',
            'manufacture_year',
            'region',
            'current_location',
            'image',
            'price_range_from',
            'price_range_to',
            'owner_name',
            'owner_email',
            'owner_contact',
            'user',
        ]



