from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("contacts/", views.ContactTemplateView.as_view(), name="contacts"),
    path('', views.ProductListView.as_view(), name='products_list'),
    path('product_details/<int:pk>/', views.ProductDetailView.as_view(), name='product_details'),
]
