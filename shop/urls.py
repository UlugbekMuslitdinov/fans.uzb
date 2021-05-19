from django.contrib import admin
from django.urls import path

from .views import CategoryListView, product_detail, CategoryDetailView, SearchResultsListView, PhoneListView, PhoneDetailView, ProductListView

app_name = 'shop'

urlpatterns = [
    path('phone/list/', PhoneListView.as_view(), name='phones'),
    path('phone/<str:slug>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('category/list/', CategoryListView.as_view(), name='categories'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('<int:id>/<str:slug>/', product_detail, name='product_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('', ProductListView.as_view(), name='product_list'),
]
