# Generated by Django 4.0.3 on 2022-05-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_invoice_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(auto_now=True),
        ),
    ]