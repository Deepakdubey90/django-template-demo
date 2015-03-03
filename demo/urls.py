from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'demo.views.home', name='home'),
                       url(r'^author-book-page/', 'demo.views.authorBookDetails'),
                       url(r'^author-book/', 'demo.views.postAuthorBookDetails'),
                       url(r'^author-book-details/', 'demo.views.index'),
                       #url(r'^demo/', include('demo.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
