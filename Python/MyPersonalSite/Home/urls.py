from django.conf.urls import patterns, url
from Home.views import homepage,addpost

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',homepage),
    url(r'add-post',addpost),
)
