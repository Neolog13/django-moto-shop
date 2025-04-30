from django.contrib.sitemaps import Sitemap

from catalog.models import Products, Categories


class MotoSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Products.objects.all()


class CategoryMotoSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Categories.objects.all()
    