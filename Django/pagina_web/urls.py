from django.urls import path
from .views import vistaPagina

urlpatterns=[
    path('',vistaPagina,name='Page')
]