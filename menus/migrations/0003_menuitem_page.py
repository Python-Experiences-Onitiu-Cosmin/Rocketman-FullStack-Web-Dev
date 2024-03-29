# Generated by Django 3.2.8 on 2021-10-24 16:16

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=modelcluster.fields.ParentalKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menus.menu'),
            preserve_default=False,
        ),
    ]
