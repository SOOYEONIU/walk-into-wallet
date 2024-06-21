from django.urls import path
from walkIntoWallet_app import views

urlpatterns = [
    path('get_data/', views.get_data, name='get_data'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_budget/', views.add_budget, name='add_budget'),
    path('update_income/<int:id>/', views.update_income, name='update_income'),
    path('update_expense/<int:id>/', views.update_expense, name='update_expense'),
    path('update_budget/<int:id>/', views.update_budget, name='update_budget'),
    path('delete_income/<int:id>/', views.delete_income, name='delete_income'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
    path('delete_budget/<int:id>/', views.delete_budget, name='delete_budget'),
]
