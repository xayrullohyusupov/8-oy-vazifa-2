from django.urls import path
from .views import CategoryListView, CategoryDetailView, ProductListView, ProductDetailView,RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    # Auth URLs
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
