from django.conf.urls import patterns, include, url
from django.contrib import admin
#from radpress.views import ArticleListView, ArticleDetailView

from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lafg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="index.html"),
        name='home'), 
    #url(r'^$', 'mysite1.boroughs.views.index'), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^films/', include('films.urls')),
    url(r'^users/', include('users.urls')),
)
