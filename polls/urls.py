from django.urls import path
from . import models

urlpatterns = [

    path("", views.index, name="index"),
    
]