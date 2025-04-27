from django.views.generic import DetailView, ListView

from catalog.models import Categories, Products
from catalog.utils import q_search


#Displays a list of categories with a custom title
class CategoriesView(ListView):
    queryset = Categories.objects.all()

    template_name = "catalog/catalog.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Categories"
        context["is_catalog_active"] = self.request.path.startswith('/catalog/')
        return context


# Displays a list of products in a specific category with filtering, ordering, and pagination.
class CatalogView(ListView):
    model = Products
    template_name = "catalog/category.html"
    context_object_name = "products"
    paginate_by = 3
    # allow_empty = False
    slug_url_kwarg = "category_slug"


    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")
        if not category_slug:
            products = super().get_queryset()
        else:
            products = super().get_queryset().filter(category__slug=category_slug)

        if query:
            products = q_search(query)

        if order_by and order_by != "default":
            products = products.order_by(order_by)

        return products


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Catalog"
        context["slug_url"] = self.kwargs.get(self.slug_url_kwarg)
        context["categories"] = Categories.objects.all()
        context["is_catalog_active"] = self.request.path.startswith('/catalog/')
        if not context["products"]:
            context["message"] = "No products found in this category"

        return context


# Displays detailed information about a specific product based on its slug.
class ProductView(DetailView):
    template_name = "catalog/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.object.name
        context["is_catalog_active"] = self.request.path.startswith('/catalog/')
        return context
