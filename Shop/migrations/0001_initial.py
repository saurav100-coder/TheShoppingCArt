# Generated by Django 3.1.7 on 2021-04-24 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.IntegerField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderid', models.IntegerField(primary_key=True, serialize=False)),
                ('status1', models.CharField(max_length=150)),
                ('status2', models.CharField(max_length=150)),
                ('status3', models.CharField(max_length=150)),
                ('status4', models.CharField(max_length=150)),
                ('invoice', models.IntegerField()),
                ('no_of_items', models.IntegerField()),
                ('order_date', models.DateField(auto_now_add=True)),
                ('shipping_date', models.DateField()),
                ('shipping_address', models.TextField(max_length=250)),
                ('is_shipped', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.seller')),
            ],
        ),
    ]
