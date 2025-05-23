# Generated by Django 4.2.18 on 2025-05-01 11:03

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_categories_description_categories_image"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="products",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.SearchVector(
                    "name", "description", config="simple"
                ),
                name="product_search_vector_idx",
            ),
        ),
    ]
