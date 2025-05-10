from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector
from django.db import models
from django.urls import reverse


class Categories(models.Model):
    """
    Represents a product category with optional description and image.
    """

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(
        upload_to="categories_images", blank=True, null=True, verbose_name="Image"
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category", kwargs={"category_slug": self.slug})


class Products(models.Model):
    """
    Represents a product with name, price, category, and optional image/description.
    Supports full-text search indexing.
    """

    name = models.CharField(max_length=150, unique=True, verbose_name="Title")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(
        upload_to="products_images", blank=True, null=True, verbose_name="Image"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Price"
    )
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Category"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            GinIndex(
                SearchVector("name", "description", config="simple"),
                name="product_search_vector_idx",
            ),
        ]

    def __str__(self):
        return f"{self.name} price = {self.price}"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        """
        Returns the product ID as a zero-padded 5-digit string.
        """
        return f"{self.id:05}"

    def sell_price(self):
        """
        Returns the final price of the product.
        """
        return self.price
