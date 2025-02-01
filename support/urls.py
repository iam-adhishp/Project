from django.urls import path
from . import views

urlpatterns = [
    path('cs/', views.cs, name='cs'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('try/', views.sampl, name='try'),
    path('sell/', views.bestsellers_list, name='bestsellers_list'),
]

