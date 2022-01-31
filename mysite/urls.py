
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from blog.views import home_view, policy_view, affiliate_view
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from blog.models import Post

#sitemap
class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

sitemaps = {'blog':BlogSitemap}

urlpatterns = [
path('admin', admin.site.urls),
  path('', home_view, name='home'),
  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path("", include("blog.urls", namespace="blog")),
    path('policy', policy_view, name='policy'),
    path("blog/affiliate", affiliate_view, name="affiliate"),
    path("", include("apis.urls", namespace="apis")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
