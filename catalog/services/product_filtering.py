import logging
from django.core.exceptions import FieldError

from catalog.models import Products
from catalog.utils import q_search


logger = logging.getLogger(__name__)


# Filters products by category, full-text query, and sorting order.
def filter_products(category_slug=None, query=None, order_by=None):
    """
    Returns a queryset of products filtered by category slug, full-text search query,
    and sorted by the specified field if valid.

    Args:
        category_slug (str, optional): Slug of the product category to filter by.
        query (str, optional): Full-text search string for product name and description.
        order_by (str, optional): Field name to sort the results by.

    Returns:
        QuerySet: Filtered and sorted list of products.
    """
    products = Products.objects.all()

    if category_slug:
        products = products.filter(category__slug=category_slug)

    if query:
        products = q_search(query)

    if order_by and order_by != "default":
        try:
            products = products.order_by(order_by)
        except FieldError as e:
            logger.warning("[order_by] Invalid field: '%s'. Error: %s", order_by, e)

    if not products.ordered:
        products = products.order_by("id")

    return products
