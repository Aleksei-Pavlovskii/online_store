from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = "catalog"

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("contacts/", views.ContactTemplateView.as_view(), name="contacts"),
    path("", views.ProductListView.as_view(), name="product_list"),
    path(
        "product_details/<int:pk>/",
        cache_page(60)(views.ProductDetailView.as_view()),
        name="product_details",
    ),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product/delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path('product_by_category/<int:pk>/', views.ProductByCategory.as_view(), name='product_by_category'),
]
