
from django.db import models
# Create your models here.
import datetime

class finaldb(models.Model):
    text =models.CharField(max_length=25114,null=True,blank=True)



class Invoice(models.Model):
    customer = models.CharField(max_length=100,primary_key=True)
    customer_email = models.EmailField(null=True,blank=True)
    billing_address = models.TextField(null=True,blank=True)
    provider_name = models.TextField(null=True,blank=True)
    provider_pin = models.TextField(null=True,blank=True)
    provider_city = models.TextField(null=True,blank=True)    
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    invoice_image = models.ImageField(upload_to='images/',blank=True, null=True)
    date = models.DateField(null=True,blank=True)
    
    
    def __str__(self):
        return str(self.customer)
    
    def get_status(self):
        return self.status

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.rate
        super(LineItem,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.customer)  
    
class UploadImage(models.Model):  
    caption = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='images')  
  
    def __str__(self):  
        return self.caption 
    

class Hotel(models.Model):
    customer = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    invoice_image = models.ImageField(upload_to='images/')
    invoice_image_results = models.ImageField(upload_to='images/results/',blank=True, null=True)    