# Generated by Django 4.0.6 on 2023-06-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0024_alter_portfolio_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]