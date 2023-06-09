# Generated by Django 4.1.7 on 2023-04-12 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_Name', models.CharField(max_length=20)),
                ('Brand_Email', models.EmailField(max_length=254, null=True)),
                ('Brand_Password', models.CharField(max_length=20, null=True)),
                ('Brand_Address', models.TextField(null=True)),
                ('Brand_City', models.CharField(max_length=25, null=True)),
                ('Brand_State', models.CharField(max_length=20, null=True)),
                ('Brand_Zip', models.CharField(max_length=15, null=True)),
                ('Brands_Logo', models.ImageField(null=True, upload_to='Brands_Logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=40)),
                ('Product_Price', models.CharField(max_length=20)),
                ('Product_Category', models.CharField(max_length=20)),
                ('Product_Description', models.TextField(max_length=200)),
                ('Product_Stock', models.IntegerField(default=0)),
                ('Product_Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
        migrations.CreateModel(
            name='PImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Image', models.ImageField(upload_to='Product_Images/')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='brand.product')),
            ],
        ),
    ]
