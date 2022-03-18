"""AppStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.Customers, name='Customers'),
    path('add', app.views.add, name='add'),
    
    path('view/<str:id>', app.views.view, name='view'),
    path('edit/<str:id>', app.views.edit, name='edit'),
    path('Listings', app.views.Listings, name='Listings'),
    path('Listings/view/<str:id>', app.views.view_Listings, name='view_Listings'), #the html files button href will refer to path(this,X,X)
    path('Listings/edit/<str:id>', app.views.edit_Listings, name='edit_Listings'),
    path('Unavailable', app.views.Unavailable, name='Unavailable'),
    path('Rentals', app.views.Rentals, name='Rentals'),
]
