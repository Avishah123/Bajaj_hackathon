from django.shortcuts import render
from django.forms.models import ModelForm, modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from .models import LineItem, Invoice
from .forms import LineItemFormset, InvoiceForm, Product_update_form, AuthorBooksFormset, OrderForm
from django.views import generic

from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, FormView)

from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from .forms import UserImageForm,HotelForm



def hotel_image_view(request):
  
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
  
        if form.is_valid():
            
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'image_new.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')



def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'image_form.html', {'form': form})  





# Create your views here.
def home(request):         
    return render(request,'index.html')

def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices,
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = LineItemFormset(request.GET or None)
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset(request.POST)
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            invoice = Invoice.objects.create(customer=form.data["customer"],
                    customer_email=form.data["customer_email"],
                    provider_name= form.data["customer_email"],
                    
                    provider_pin= form.data["provider_pin"],
                    provider_city= form.data["provider_city"],
                    billing_address=form.data["billing_address"],
                    date=form.data["date"],
                    
                    
                    )
            # invoice.save()

        if formset.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            total = 0
            for form in formset:
                service = form.cleaned_data.get('service')
                description = form.cleaned_data.get('description')
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')
                if service and description and quantity and rate:
                    amount = float(rate)*float(quantity)
                    total += amount
                    LineItem(customer=invoice,
                            service=service,
                            description=description,
                            quantity=quantity,
                            rate=rate,
                            amount=amount).save()
            invoice.total_amount = total
            invoice.save()
            try:
                print('done and dusted')
            except Exception as e:
                print(f"********{e}********")
            return redirect('/')
    context = {
        "title": "Invoice Generator",
        "formset": formset,
        "form": form,
        # "customer" : Invoice.objects.values('customer'),
    }
    return render(request, 'invoice-create.html', context)

