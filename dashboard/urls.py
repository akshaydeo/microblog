from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'post/$', 'dashboard.views.post'),
    url(r'$', 'dashboard.views.dashboard'),    
)