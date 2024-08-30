# Generated by Django 5.0.7 on 2024-07-20 19:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Категория продуктов",
                "verbose_name_plural": "Категории продуктов",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category", "purchase_price"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.RenameField(
            model_name="category",
            old_name="category_description",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="category_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="product_description",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="product_name",
            new_name="name",
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                help_text="Введите категорию продукта",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="catalog.category",
                verbose_name="Категория продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания продукта",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="purchase_price",
            field=models.IntegerField(
                help_text="Введите цену продукта", verbose_name="Цена продукта"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата изменения продукта",
            ),
            preserve_default=False,
        ),
    ]
