from django.contrib.sitemaps import Sitemap
from .models import Stih


class StihSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Stih.objects.all()

    def lastmod(self, obj):
        return obj.updated