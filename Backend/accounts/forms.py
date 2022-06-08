from django import forms
from django.forms import formset_factory
from .models import *
from django.forms.models import inlineformset_factory
from django.db import transaction

class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
        
    @transaction.atomic  
    def save(self):       
        print('inside save function of ')
        name = self.cleaned_data.get('name')
        print(name)        
        attendance = Hotel(name=self.cleaned_data.get('name'),hotel_Main_Img=self.cleaned_data.get('hotel_Main_Img'))
        attendance.save()


class UserImageForm(forms.ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        models = UploadImage  
        # It includes all the fields of model  
        fields = '__all__'  



class InvoiceForm(forms.Form):
    
        # fields = ['customer', 'message']
    customer = forms.CharField(
        label='Cusomter',
        
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer ID',
            'rows':1    
        }
        
    )
    )
    customer_email = forms.CharField(
        label='Customer Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'customer@company.com',
            'rows':1
        })
    )
    billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )
    provider_name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'rows':1
        })
    )
    
    provider_pin = forms.CharField(
        label='Pincode',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Pincode',
            'rows':1
        })
    )
    
    provider_city = forms.CharField(
        label='city',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'city',
            'rows':1
        })
    )
    
    date = forms.CharField(
        label='date',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'date',
            'rows':1
        })
    )
    
    
   

class LineItemForm(forms.Form):
    
    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Service Name'
        })
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter Book Name here',
            "rows":1
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate'
        })
    )



    
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)

class Product_update_form(forms.ModelForm):
    class Meta:
        model = LineItem
        fields = ['service','description','quantity','rate']

AuthorBooksFormset = inlineformset_factory(Invoice,LineItem, fields=('service',))

class OrderForm(forms.ModelForm):
	class Meta:
		model = LineItem
		fields = '__all__'