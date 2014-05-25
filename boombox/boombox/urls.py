from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
# Examples:
# url(r'^$', 'boombox.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'profiles.views.show_profile'),
    url(r'^users/(?P<user_slug>[a-z0-9-]+)/$', 'profiles.views.show_user'),
    url(r'^users/$', 'profiles.views.show_users'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'profiles.views.index')
)
