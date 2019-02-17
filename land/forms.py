from django import forms

from .models import Let_Land, Lease_Let_Land, Request_To_Lease, Request_To_Lease_Offer, Sell_Land, Buy_Land, Request_To_Buy, Request_To_Buy_Offer


class let_Land_Form(forms.ModelForm):

    class Meta:
        model = Let_Land
        exclude = ('user',)

        widgets = {   

            'land_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter land size', 'required': True}),                        
            'crop_grown': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nearest Town', 'required': True}),
            
           
            'water_source': forms.Select(attrs={'class': 'form-control', 'required': True}), 
            'lease_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lease Period', 'required': True}),
            
            'price_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Name', 'required': True}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Owner Email Address', 'required': True}),
            'owner_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Contact Details', 'required': True}),
                               

        }

        fields = [            
    
            'land_size',
            'crop_grown',
            'region',
            'location',
            'nearest_town',
            'water_source',
            'lease_period',

            'price_per',
            'price',
            'owner_name',
            'owner_email',
            'owner_contact',
            'user',
        ]


class lease_Let_Land_Form(forms.ModelForm):

    class Meta:
        model = Lease_Let_Land
        exclude = ('user', 'let_land')

        widgets = {   
                      
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Details', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'price_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),
            'lease_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lease Period', 'required': True}),
            'crop_to_grow': forms.Select(attrs={'class': 'form-control', 'required': True}),
                               

        }

        fields = [            

            'name',
            'email',
            'contact',            
            'price',
            'price_per',
            'lease_period',
            'crop_to_grow',

            'let_land',
            'user',
        ]


class request_To_Lease_Form(forms.ModelForm):

    class Meta:
        model = Request_To_Lease
        exclude = ('user',)

        widgets = { 

            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'land_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter land size', 'required': True}),
            
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nearest Town', 'required': True}),
            'lease_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lease Period', 'required': True}),
            
            'price_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Details', 'required': True}),            
                               

        }

        fields = [            
            
            'region',
            'land_size',            
            'location',
            'nearest_town',
            'lease_period',

            'price_per',
            'price',
            'name',
            'email',
            'contact',
            'user',
        ]



class request_To_Lease_Offer_Form(forms.ModelForm):

    class Meta:
        model = Request_To_Lease_Offer
        exclude = ('user', 'request_to_lease')

        widgets = {   
                      
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Details', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'price_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),
            
                               

        }

        fields = [            

            'name',
            'email',
            'contact',  
            'location',          
            'price',
            'price_per',

            'request_to_lease',
            'user',
        ]





class sell_Land_Form(forms.ModelForm):

    class Meta:
        model = Sell_Land
        exclude = ('user',)

        widgets = { 

            'land_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter land size', 'required': True}),
            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'specific_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Specific Location', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nearest Town', 'required': True}),                        
            'price_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'price_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),          
            
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'owner_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Details', 'required': True}),            
                               

        }

        fields = [            
            'land_size',
            'region',            
            'specific_location',
            'nearest_town',
            'price_range',
            'price_per',
            'owner_name',
            'owner_email',
            'owner_contact',
            'user',
        ]


class buy_Land_Form(forms.ModelForm):

    class Meta:
        model = Buy_Land
        exclude = ('user', 'sell_land')

        widgets = {              
            
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Details', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'price_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            
                               

        }

        fields = [            
            
            'price',
            'price_per',
            'name',
            'email',
            'contact',  
            'sell_land',
            'user',
        ]



class request_To_Buy_Form(forms.ModelForm):

    class Meta:
        model = Request_To_Buy
        exclude = ('user',)

        widgets = { 

            'region': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'land_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter land size', 'required': True}),                       
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location', 'required': True}),
            'nearest_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nearest Town', 'required': True}),
            'price_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),          
            'price_range_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),
            
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Details', 'required': True}),            
                               

        }

        fields = [            
            
            'region',
            'land_size',           
            'location',
            'nearest_town',
            'price_range',
            'price_range_per',
            'name',
            'email',
            'contact',
            'user',
        ]



class request_To_Buy_Offer_Form(forms.ModelForm):

    class Meta:
        model = Request_To_Buy_Offer
        exclude = ('user', 'request_to_buy')

        widgets = {   
                      
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Details', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price in Ksh', 'required': True}),
            'price_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price Per', 'required': True}),
            
                               

        }

        fields = [            

            'name',
            'email',
            'contact',  
            'location',          
            'price',
            'price_per',
            'request_to_buy',
            'user',
        ]


