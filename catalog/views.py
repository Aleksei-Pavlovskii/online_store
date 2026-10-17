from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    CreateView,
    DeleteView,
)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    template_name = "catalog/product_delete.html"

    def dispatch(self, request, *args, **kwargs):
        """Удалять может владелец или модератор."""
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = request.user.has_perm("catalog.can_unpublish_product")

        if not (is_owner or is_moderator):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class HomeView(TemplateView):
    template_name = "catalog/home.html"
