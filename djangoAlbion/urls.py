from django.contrib import admin
from django.urls import path

from market.views import *
from django.urls import path, include

urlpatterns = [
    path('', include('market.urls'))
]

handler404 = pageNotFound
