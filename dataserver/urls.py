from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from dataserver import views



urlpatterns = [
    url(r'^dataserver/$',views.get_item),
]