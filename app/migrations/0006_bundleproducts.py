# Generated by Django 2.2.4 on 2020-04-04 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200404_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='BundleProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_child', to='app.ProductsModel')),
                ('product_bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_bundle', to='app.ProductsModel')),
            ],
        ),
    ]
