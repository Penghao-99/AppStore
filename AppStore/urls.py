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
    path('add_newcustomer', app.views.add_newcustomer, name='add_newcustomer'),
    path('add_newlisting', app.views.add_newlisting, name='add_newlisting'),
    path('add_newunavailable', app.views.add_newunavailable, name='add_newunavailable'),
    path('add_newrental', app.views.add_newrental, name='add_newrental'),
    path('Customers', app.views.Customers, name='Customers'),
    path('Customers/edit/<str:id>', app.views.edit_Customers, name='edit_Customers'),
    path('Listings', app.views.Listings, name='Listings'),
    path('Listings/view/<str:id>', app.views.view_Listings, name='view_Listings'), #the html files button href will refer to path(this,X,X)
    path('Listings/edit/<str:id>', app.views.edit_Listings, name='edit_Listings'),
    path('Unavailable', app.views.Unavailable, name='Unavailable'),
    path('Unavailable/view/<str:id>', app.views.view_Unavailable, name='view_Unavailable'), 
    path('Unavailable/edit/<str:id>', app.views.edit_Unavailable, name='edit_Unavailable'),
    path('Rentals', app.views.Rentals, name='Rentals'),
    path('Rentals/view/<str:id>', app.views.view_Rentals, name='view_Rentals'), 
    path('Rentals/edit/<str:id>', app.views.edit_Rentals, name='edit_Rentals'),
]
