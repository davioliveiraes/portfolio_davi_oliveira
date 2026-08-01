from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    protocol = "https"
    i18n = True
    alternates = True

    def items(self):
        # One-page: as URLs antigas são redirects 301 e ficam fora do sitemap
        return ["core:home"]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0 if item == "core:home" else 0.8
