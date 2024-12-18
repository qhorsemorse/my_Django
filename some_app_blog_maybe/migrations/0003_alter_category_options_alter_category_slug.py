# Generated by Django 5.1 on 2024-10-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('some_app_blog_maybe', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації', 'verbose_name_plural': 'Категорії для публікацій'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Слаг'),
        ),
    ]
