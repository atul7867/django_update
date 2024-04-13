from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.add,name="add"),
    path("show",views.show,name="show"),
    path("rem",views.rem,name="rem"),
    path("rem/<int:fac_id>",views.rem,name="rem"),
    path("ser",views.ser,name="ser"),
    path("up",views.up,name="up"),

    
]
