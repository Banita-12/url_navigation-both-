from specific.views import *
from django.urls import path
app_name='3idiots'
urlpatterns=[
    path('rancho/',rancho,name='rancho'),
    path('raju/',raju,name='raju')
]