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
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
]
