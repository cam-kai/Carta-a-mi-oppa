from django.urls import path, include
from .views import carta

urlpatterns=[
    path('', carta, name= 'carta')
]