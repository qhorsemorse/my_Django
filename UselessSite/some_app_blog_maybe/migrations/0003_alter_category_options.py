# Generated by Django 5.1.1 on 2024-10-14 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('some_app_blog_maybe', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації', 'verbose_name_plural': 'Категорії для публікацій'},
        ),
    ]