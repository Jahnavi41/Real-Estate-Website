from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('add-listing/', views.add_listing, name='add_listing'),
    path('manage-listings/', views.manage_listings, name='manage_listings'),
    path('my-listings/', views.user_listings, name='user_listings'),
    path('listing/edit/<int:pk>/', views.edit_listing, name='edit_listing'),
    path('listing/delete/<int:pk>/', views.delete_listing, name='delete_listing'),
]