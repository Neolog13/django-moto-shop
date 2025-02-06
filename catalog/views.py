from django.shortcuts import render

from catalog.models import Categories, Products


def catalog(request):

    products = Products.objects.all()

    categories = Categories.objects.all()


    context = {
        "title": 'Home - catalog',
        "categories": categories,
        "products": products,
    }
    #[
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb650r-pearl_smoky_gray-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-scl500-matte_black_metallic-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2025-cb500f-matte_black_metallic-1505x923',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2025-cb500f-matte_black_metallic-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    #     {
    #         "image": 'images/foto_bikes/2024-cb1000r-black-edition-black-1505x923.avif',
    #         "name": 'djsfkhgklj',
    #         "description": 'sdljkfhgks',
    #         "price":'324234',
    #     },
    # ],


    return render(request, 'catalog/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context=context)
