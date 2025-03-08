# 8:29:49

from django.core.paginator import Paginator
from django.shortcuts import render

from catalog.models import Categories, Products
from catalog.utils import q_search


def catalog_categories(request):
    categories = Categories.objects.all()
    context = {
        "title": 'Home - catalog',
        "categories": categories,
    }
    return render(request, 'catalog/catalog.html', context=context)


def catalog_products(request, category_slug=None):

    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    
    query = request.GET.get('q', None)

    categories = Categories.objects.all()
    products = Products.objects.filter(category__slug=category_slug)

    if query:
        products = q_search(query)


    if order_by and order_by != "default":
        products = products.order_by(order_by)



    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": 'Home - catalog',
        "categories": categories,
        "products": current_page,
        "slug_url": category_slug,
    }
    return render(request, 'catalog/category.html', context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context=context)
