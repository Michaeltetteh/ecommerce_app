# Generated by Django 2.2.3 on 2019-08-03 22:02

from django.db import migrations


def capitalize(apps, schema_editor):
    Product = apps.get_model('main', 'Product')
    for product in Product.objects.all():
        product.name = product.name.capitalize()
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_productimage_thumbnail'),
    ]

    operations = [
        migrations.RunPython(
            capitalize,
            migrations.RunPython.noop
        )
    ]
