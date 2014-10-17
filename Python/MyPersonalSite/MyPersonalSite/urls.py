from django.conf.urls import include, url
from django.contrib import admin
import Home.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'MyPersonalSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include(Home.urls)),
]
