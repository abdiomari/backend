# Generated by Django 4.2.1 on 2023-05-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_order_alter_products_price_alter_products_rating_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
