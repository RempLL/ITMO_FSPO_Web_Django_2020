# Generated by Django 3.0.6 on 2020-06-22 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0004_auto_20200623_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='dishes',
            field=models.ManyToManyField(blank=True, to='restaurant_app.Dishes'),
        ),
    ]
