from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from catalog.models import Product


def q_search(query):
    """
    Full-text PostgreSQL search for products by name and description,
    ordered by relevance and highlighted in results.

    Args:
        query (str): The search phrase provided by the user.

    Returns:
        QuerySet: Filtered and annotated list of products.
    """

    search_vector = SearchVector("name", "description")
    search_query = SearchQuery(query)

    products = (
        Product.objects.annotate(rank=SearchRank(search_vector, search_query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    products = products.annotate(
        headline=SearchHeadline(
            "name", search_query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    products = products.annotate(
        bodyline=SearchHeadline(
            "description", search_query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return products
