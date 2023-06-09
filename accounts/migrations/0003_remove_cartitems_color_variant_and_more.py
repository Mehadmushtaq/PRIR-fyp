# Generated by Django 4.0.2 on 2023-04-26 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_product_slug'),
        ('accounts', '0002_cart_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='color_variant',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='size_variant',
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='brand.product'),
        ),
    ]
