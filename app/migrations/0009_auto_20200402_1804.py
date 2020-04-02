# Generated by Django 3.0.2 on 2020-04-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200402_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='organization_type',
            field=models.IntegerField(choices=[(1, 'Individual'), (2, 'Proprietorship'), (4, 'Partnership'), (5, 'Trust'), (6, 'Gvt Organisation')], db_index=True, default=1),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='tax',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, default=0.0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organization_type',
            field=models.IntegerField(choices=[(1, 'Individual'), (2, 'Proprietorship'), (4, 'Partnership'), (5, 'Trust'), (6, 'Gvt Organisation')], db_index=True, default=1),
        ),
    ]
