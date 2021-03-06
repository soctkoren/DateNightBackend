from django.urls import path, include

from datenight_backend.apis.v1 import *

urlpatterns = [
    path('', index, name='index'),
    path('initialize_create_flow', initialize_create_flow, name='initialize_create_flow'),
    path('upload_date_hero_img', upload_date_hero_img, name='upload_date_hero_img'),
    path('date', date, name='date'),
    path('node', node, name='node'),
]
