from django.urls import path    
from . import views

urlpatterns = [
    path('dashboard/', views.home, name='dashboard-home'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('order/', views.order, name='dashboard-order'),
    path('product/', views.product, name='dashboard-product'),
    path('about/', views.AboutView.as_view())
]