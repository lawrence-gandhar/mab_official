# Generated by Django 2.2.4 on 2020-04-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200402_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_address_details',
            name='is_shipping_address',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True),
        ),
    ]
