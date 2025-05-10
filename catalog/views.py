from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import DetailView, ListView

from catalog.models import Categories, Products
from catalog.services.product_filtering import filter_products


class CategoriesView(ListView):
    """
    View for displaying all available product categories.

    Attributes:
        queryset (QuerySet): All category objects.
        template_name (str): Template for rendering the categories.
        context_object_name (str): Context variable name for template access.
    """

    queryset = Categories.objects.all()
    template_name = "catalog/catalog.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        """
        Adds custom context variables for template rendering.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Categories"
        context["is_catalog_active"] = self.request.path.startswith("/catalog/")
        return context


class CatalogView(ListView):
    """
    View for displaying a list of products within a specific category,
    with support for full-text search, sorting, and pagination.

    Attributes:
        model (Model): Product model.
        template_name (str): Template for rendering products.
        context_object_name (str): Context variable name for products.
        paginate_by (int): Number of products per page.
        slug_url_kwarg (str): URL keyword argument for category slug.
    """

    model = Products
    template_name = "catalog/category.html"
    context_object_name = "products"
    paginate_by = 3
    slug_url_kwarg = "category_slug"

    def get_queryset(self):
        """
        Returns a filtered and sorted queryset of products based on URL and query parameters.
        """
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        query = self.request.GET.get("q")
        order_by = self.request.GET.get("order_by")

        return filter_products(
            category_slug=category_slug, query=query, order_by=order_by
        )

    def paginate_queryset(self, queryset, page_size):
        """
        Paginates the given queryset while gracefully handling invalid, missing, or out-of-range page numbers.

        Falls back to the first page if the page number is invalid (non-integer or missing),
        and to the last page if the requested page exceeds the total number of pages.

        Args:
            queryset (QuerySet): The list of items to paginate.
            page_size (int): The number of items per page.

        Returns:
            tuple: A tuple containing the paginator, page object, list of items on the current page,
            and a boolean indicating whether pagination is needed.
        """
        paginator = Paginator(queryset, page_size)
        page = self.request.GET.get("page")

        try:
            page_number = int(page)
        except (TypeError, ValueError):
            page_number = 1

        try:
            page_obj = paginator.page(page_number)
        except (EmptyPage, PageNotAnInteger):
            page_obj = paginator.page(paginator.num_pages)

        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())

    def get_context_data(self, **kwargs):
        """
        Adds extra context variables for the product listing view.
        """
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Home - Catalog",
                "slug_url": self.kwargs.get(self.slug_url_kwarg),
                "categories": Categories.objects.all(),
                "is_catalog_active": self.request.path.startswith("/catalog/"),
            }
        )

        if not context["products"]:
            context["message"] = "No products found in this category"

        return context


class ProductView(DetailView):
    """
    View for displaying detailed information about a single product.

    Attributes:
        template_name (str): Template for product detail page.
        slug_url_kwarg (str): URL keyword argument for product slug.
        context_object_name (str): Context variable name for the product.
    """

    template_name = "catalog/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        """
        Retrieves a product instance based on its slug.
        """
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the product detail view.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        context["is_catalog_active"] = self.request.path.startswith("/catalog/")
        return context
