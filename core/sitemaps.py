from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'
    template_name = 'sitemap.xml'

    def items(self):
        return ['core:index', 'core:about', 'core:contact']  # URL names defined in your urls.py

    def location(self, item):
        return reverse(item)
