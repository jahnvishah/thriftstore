# Generated by Django 3.0.7 on 2020-10-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201024_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lattitude',
            field=models.DecimalField(decimal_places=2, default=565555, max_digits=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='longitude',
            field=models.DecimalField(decimal_places=2, default=4545333, max_digits=10000),
            preserve_default=False,
        ),
    ]
