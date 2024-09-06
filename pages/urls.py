from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_realtor/', views.special, name='special_page'),
    path('listing_approval',views.approval, name='approval')
]