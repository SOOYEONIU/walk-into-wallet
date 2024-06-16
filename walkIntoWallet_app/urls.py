from django.urls import path
from walkIntoWallet_app import views

urlpatterns = [
    path('index/', views.index),
]
