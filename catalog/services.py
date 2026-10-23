from catalog import models
from django.core.cache import cache

CACHE_MISS = object()

def get_products_by_category(category_id):
    my_key = f'products_by_category:{category_id}'
    data = cache.get(my_key, CACHE_MISS)

    if data is CACHE_MISS:
        products = models.Product.objects.filter(category_id=category_id)
        data = list(products)
        cache.set(my_key, data, 60 * 15)

    return data

def invalidate_product_by_category_cache(category_id):
    cache.delete(f'products_by_category:{category_id}')