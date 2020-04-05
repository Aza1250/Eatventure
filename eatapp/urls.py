"""eatapp URL Configuration

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
from django.urls import include, path, re_path

urlpatterns = [
    path('', include('frontend.urls')),
    re_path(r'^search/(?P<restaurant_name>[\w|\W]+)/(?P<street_name>[\w|\W]+)/(?P<postcode>[\w|\W]+)/', include('frontend.urls')),
    path('mapstats/', include('frontend.urls')),
    path('login/', include('restaurant_management.urls')),
    path('login/<slug:username>/<slug:password>/', include('restaurant_management.urls')),
    path('login/<slug:username>/<slug:password>/<slug:restaurant_id>/', include('restaurant_management.urls')),
    re_path(r'^(?P<username>[\w|\W]+)/(?P<password>[\w|\W]+)/(?P<restaurant_id>[\w|\W]+)/update/(?P<restaurant_name>[\w|\W]+)/(?P<best_selling_item>[\w|\W]+)/(?P<best_selling_item_dsc>[\w|\W]+)/(?P<food_bank>[\w|\W]+)/', include('restaurant_management.urls')),
    path('login/<slug:username>/<slug:password>/<slug:restaurant_id>/delete/', include('restaurant_management.urls')),
    path('admin/', admin.site.urls),
]
