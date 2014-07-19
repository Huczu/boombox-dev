from django.conf.urls import patterns, include, url

from django.contrib import admin
from misc.views import LatestLinkView, TagView, TagDetailView

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LatestLinkView.as_view(), name="latest"),
    url(r'^tag/(?P<pk>\d+)$', TagDetailView.as_view(), name="tag_detail"),
    url(r'^tag/$', TagView.as_view(), name="tag"),
)

