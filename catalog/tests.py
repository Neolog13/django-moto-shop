from django.test import TestCase
from django.urls import reverse

from catalog.models import Product



class GetPagesTestCase(TestCase):
    fixtures = ['fixtures/catalog/categories.json', 'fixtures/catalog/products.json']

    def setUp(self):
        "initialization before executing the first test"

    def test_data_catalog(self):
        products = Product.objects.all()

        path = reverse('catalog:index')
        response = self.client.get(path)

        self.assertQuerySetEqual(list(response.context_data['products'][:3]), [product for product in products[:3]])

    def test_paginate_catalog(self):
        path = reverse('catalog:index')
        page = 2
        paginate_by = 3
        response = self.client.get(path + f'?page={page}')
        products = Product.objects.all()
        self.assertQuerySetEqual(list(response.context_data['products']), products[(page - 1) * paginate_by:page * paginate_by])

    def test_content_product(self):
        product = Product.objects.get(pk=1)
        path = reverse('catalog:product', args=[product.slug])
        response = self.client.get(path)
        self.assertEqual(product.description, response.context_data['product'].description)

    def tearDown(self):
        "actions after test execution"


"python manage.py test ."
"python manage.py test catalog"