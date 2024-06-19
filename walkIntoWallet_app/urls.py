from django.urls import path
from walkIntoWallet_app import views

urlpatterns = [
    path('get_data/', views.get_data, name='get_data'),
]
