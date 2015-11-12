from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kepler_responsor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    (r'^',include('kepler_responsor_app.urls')),
    #(r'^kepler/',include('kepler_responsor_app.urls')),
)
