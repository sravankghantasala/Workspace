from django.conf.urls import patterns, url
from myhome.views import homepage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',homepage),
)
