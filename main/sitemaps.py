from django.contrib.sitemaps import Sitemap

from catalog.models import Product, Category


class MotoSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Product.objects.all()


class CategoryMotoSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Category.objects.all()
    