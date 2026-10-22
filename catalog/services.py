from catalog import models


def get_products_by_category(catуgory_id):
    products = models.Product.objects.filter(category_id=catуgory_id)
    return list(products)

