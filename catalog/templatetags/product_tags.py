from django import template

from catalog.models import Products


register = template.Library()


@register.simple_tag()
def tag_products():
    """
    Returns a queryset of all products
    """
    return Products.objects.all()
