# Generated by Django 2.2.6 on 2020-08-04 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_isincentive'),
        ('Incentives_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productincentives',
            name='products',
        ),
        migrations.AddField(
            model_name='productincentives',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
    ]
