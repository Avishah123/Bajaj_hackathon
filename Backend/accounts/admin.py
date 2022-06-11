from django.contrib import admin
from .models import Invoice, LineItem,Hotel

# Register your models here.

admin.site.register(Invoice)
admin.site.register(LineItem)
admin.site.register(Hotel)