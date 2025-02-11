from django import template
from django.core.paginator import Paginator
from catalog.models import Categories, Products


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


# @register.simple_tag()
# def tag_products():
#     return Products.objects.all()


@register.simple_tag
def tag_products(page_number=1, products_per_page=3):
    products = Products.objects.all()
    paginator = Paginator(products, products_per_page)  # Создаем объект Paginator

    try:
        page = paginator.page(page_number)  # Получаем нужную страницу
    except Exception:
        page = paginator.page(1)  # Если страница не существует, используем первую страницу

    return page


@register.simple_tag
def tag_products_by_category(category):
    return Products.objects.filter(category=category)