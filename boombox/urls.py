from django.conf.urls import patterns, include, url

from django.contrib import admin
from boombox import settings
from misc.views import LatestLinkView, TagsListView, TagDetailView, \
    UsersListView, UserProfileDetailView, DashboardView, UserProfileEditView, \
    CreateLinkView, LinkDetailView
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LatestLinkView.as_view(), name="latest"),
    url(r'^link/(?P<pk>\d+)/(?P<slug>.+)/$', LinkDetailView.as_view(),
        name="lin"
             "k_detail"),

    url(r'^tags/(?P<slug>.+)$', TagDetailView.as_view(), name="tag_detail"),
    url(r'^tags/$', TagsListView.as_view(), name="tag"),

    url(r'^users/$', UsersListView.as_view(), name="user"),
    url(r'^users/(?P<slug>.+)/$', UserProfileDetailView.as_view(),
        name='profile'),

    url(r'^edit_profile/$',
        login_required(UserProfileEditView.as_view()), name='edit_profile'),
    url(r'^create_post/$', login_required(CreateLinkView.as_view()),
        name='create_post'),
    # url(r'^edit_link/(?P<slug>\w+)/$'),
    # url(r'^delete_link/(?P<slug>\w+)/$'),
    url(r'^dashboard/$', login_required(DashboardView.as_view()),
        name="dashboard"),
    url(r'^foundation/$', include('foundation.urls')),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
         'show_indexes': True}),
)

