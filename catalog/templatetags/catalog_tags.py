from django import template
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.http import urlencode

from catalog.models import Categories, Products


register = template.Library()


@register.simple_tag()
def tag_categories():
    """
    Returns all product categories.

    Used to display a list of categories in templates.
    """
    return Categories.objects.all()


@register.simple_tag
def tag_products(page_number=1, products_per_page=3):
    """
    Returns a paginated list of products.

    Args:
        page_number (int): The requested page number.
        products_per_page (int): Number of products per page.

    Returns:
        Page: A Django Page object containing products.
    """
    products = Products.objects.all()
    paginator = Paginator(products, products_per_page)

    try:
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page = paginator.page(1)

    return page


@register.simple_tag
def tag_products_by_category(category):
    """
    Returns products that belong to a specific category.

    Args:
        category (Category): The category to filter products by.

    Returns:
        QuerySet: Filtered products by category.
    """
    return Products.objects.filter(category=category)


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """
    Updates query parameters in the URL.

    Args:
        context (dict): Template context with the request object.
        **kwargs: Key-value pairs to update in the query string.

    Returns:
        str: Encoded URL query string.
    """
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
