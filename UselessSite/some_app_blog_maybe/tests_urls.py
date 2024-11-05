# app_blog/tests_urls.py
from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, ArticleList, ArticleDetail, ArticleCategoryList

class UrlsTests(TestCase):
    def test_home_url_resolves_home_view(self):
        url = reverse('home')
        self.assertEqual(url, '/')
        view = resolve(url)
        self.assertEqual(view.func.view_class, HomePageView)

    def test_articles_list_url_resolves(self):
        url = reverse('articles-list')
        self.assertEqual(url, '/articles/')
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleList)

    def test_article_detail_url_resolves(self):
        url = reverse('news-detail', args=[2024, 10, 14, 'sample-slug'])
        self.assertEqual(url, '/articles/2024/10/14/sample-slug/')
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleDetail)

    def test_articles_category_list_url_resolves(self):
        url = reverse('articles-category-list', args=['category-slug'])
        self.assertEqual(url, '/articles/category/category-slug/')
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleCategoryList)




