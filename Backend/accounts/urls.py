from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', InvoiceListView.as_view(), name="invoice-list"),
    path('new11',views.home,name='home'),
    path('image_upload', hotel_image_view, name = 'image_upload'),
    path('test', views.test_veiw, name = 'test'),
    path('success', success, name = 'success'),
    path('new/', views.image_request, name = "image-request"),  
    path('create/', createInvoice, name="invoice-create"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  