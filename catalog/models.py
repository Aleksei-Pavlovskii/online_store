from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", unique=True)
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Продукт")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="photos/", blank=True, null=True, verbose_name="Фото"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
        null=True,
        blank=True,
    )
    price = models.FloatField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name='Наличие товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
