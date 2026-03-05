from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'catalog/product_delete.html'


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class HomeView(TemplateView):
    template_name = "catalog/home.html"
