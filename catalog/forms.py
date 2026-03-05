from django import forms
from django.core.exceptions import ValidationError
from .constants import FORBIDDEN_WORDS

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'is_active']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})

        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите стоимость продукта'})

        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите описание продукта'})

        self.fields['image'].widget.attrs.update({'class': 'form-control'})

        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной или равняться нулю')
        return price

    def clean_name(self):
        name = self.cleaned_data['name']

        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError('В названии используется запрещенное слово')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']

        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError('В описании используется запрещенное слово')
        return description
