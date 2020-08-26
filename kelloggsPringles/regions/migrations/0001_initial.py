# Generated by Django 2.0 on 2020-08-26 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kelloggs_pringles', '0005_fairprice_shopee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singapore',
            fields=[
                ('prod_name', models.CharField(max_length=145, primary_key=True, serialize=False)),
                ('fairprice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kelloggs_pringles.Fairprice')),
            ],
        ),
    ]