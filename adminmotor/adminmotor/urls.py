from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adminmotor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup-email/', 'app.views.signup_email'),
    url(r'^email-sent/', 'app.views.validation_sent'),
    url(r'^login/$', 'app.views.home'),
    url(r'^logout/$', 'app.views.logout', name='logout'),
    url(r'^done/$', 'app.views.done', name='done'),
    url(r'^email/$', 'app.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
