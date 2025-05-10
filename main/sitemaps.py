from django.contrib.sitemaps import Sitemap
from catalog.models import Products, Categories


class MotoSitemap(Sitemap):
    """
    Sitemap for the Product model.

    This sitemap provides information about the products on the website,
    including their URLs, priority, and frequency of changes.

    Attributes:
        changefreq (str): The change frequency for the products. Default is 'monthly'.
        priority (float): The priority of the products on the website. Default is 0.9.
    """

    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Products.objects.all()


class CategoryMotoSitemap(Sitemap):
    """
    Sitemap for the Category model.

    This sitemap provides information about the categories on the website,
    including their URLs, priority, and frequency of changes.

    Attributes:
        changefreq (str): The change frequency for the categories. Default is 'monthly'.
        priority (float): The priority of the categories on the website. Default is 0.9.
    """

    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Categories.objects.all()
