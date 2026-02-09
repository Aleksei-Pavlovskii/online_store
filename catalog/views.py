from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
