# Generated by Django 2.2.4 on 2020-04-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200331_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'Cash'), (2, 'Card'), (3, 'Cheque'), (4, 'Demand Draft'), (5, 'Net Banking')], db_index=True, default=1),
        ),
        migrations.AlterField(
            model_name='collectpartial',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'Cash'), (2, 'Card'), (3, 'Cheque'), (4, 'Demand Draft'), (5, 'Net Banking')], db_index=True, default=1),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='customer_type',
            field=models.IntegerField(blank=True, choices=[(1, 'CUSTOMER'), (2, 'VENDOR'), (3, 'EMPLOYEE')], db_index=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='customer_type',
            field=models.IntegerField(blank=True, choices=[(1, 'CUSTOMER'), (2, 'VENDOR'), (3, 'EMPLOYEE')], db_index=True, default=1),
        ),
        migrations.AlterField(
            model_name='user_account_details',
            name='account_number',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_tax_details',
            name='preferred_delivery',
            field=models.IntegerField(blank=True, choices=[(0, 'Any'), (1, 'Print Later'), (2, 'Send Later')], db_index=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user_tax_details',
            name='preferred_payment_method',
            field=models.IntegerField(blank=True, choices=[(0, 'Any'), (1, 'Cash'), (2, 'Card'), (3, 'Cheque'), (4, 'Net Banking')], db_index=True, default=0, null=True),
        ),
    ]
