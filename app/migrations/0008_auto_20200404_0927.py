# Generated by Django 2.2.4 on 2020-04-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200404_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='product_type',
            field=models.IntegerField(blank=True, choices=[(0, 'GOODS'), (1, 'SERVICES'), (2, 'BUNDLE')], db_index=True, default=0, null=True),
        ),
    ]
