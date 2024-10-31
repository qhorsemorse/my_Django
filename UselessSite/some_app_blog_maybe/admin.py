'''# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (
        (None, {
            'fields': ('category',),
        }),
    )

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('title', 'image',),
        }),
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    fieldsets = (
        (None, {
            'fields': ('pub_date', 'title', 'description', 'main_page'),
        }),
        ('Додатково', {
            'classes': ('grp-collapse', 'grp-closed',),
            'fields': ('slug',),
        }),
    )

    def delete_file(self, pk, request):
        """Delete an image."""
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

admin.site.register(Article, ArticleAdmin)
'''

from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    prepopulated_fields = {'slug': ('category',)}  # Додаємо автозаповнення

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)