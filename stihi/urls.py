"""stihi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from stihinazakaz import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from stihinazakaz.sitemap import StihSitemap

sitemaps = {
    'stihi': StihSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.topics, name="topics"),
    path('pozdravleniya', views.topics, name="topics"),
    path('politics', views.politics, name="politics"),
    path('price', views.price, name="price"),
    path('feedback2', views.feedback2, name="feedback2"),
    re_path(r'^pozdravleniya/(?P<the_topic_slug>[-\w]+)/$', views.poems, name="poems"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    re_path(r'^pozdravleniya/stihi/(?P<the_poem_slug>[-\w]+)/$', views.stihi, name='stihi'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)