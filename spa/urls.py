from django.urls import path
from . import views

app_name = "spa"

urlpatterns = [
    path('', views.main_spa, name='main_spa'),
    path('<int:page>', views.main_spa, name = 'main_spa_paginate'),
    path('add_new_message/', views.add_new_message, name='add_new_message'),
    # path('payment-confirm/<int:session_id>/', views.payment_confirm, name='payment_confirm'),
    # path('tariffs/', views.tariffs, name='tariffs'),
    # path('tariff-add/', views.tariff_add, name='tariff_add'),
    # path('tariff-complete/<int:tariff_id>', views.tariff_complete, name='tariff_complete'),
]