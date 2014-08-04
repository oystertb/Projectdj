from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from films import views
from films.views import *

from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lafg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^search_form/(?P<option>\d+)/$', views.search_form, name='search_form'),
    url(r'^top_rated/$', views.top_rated, name='top_rated'),
    url(r'^film_edit/$', views.film_edit, name='film_edit'),
    url(r'^seeFilmDetail/$', views.seeFilmDetail, name='seeFilmDetail'),
    url(r'^film_add/$', views.film_add, name='film_add'),
    url(r'^searchOptions/$',views.searchOptions),
    url(r'^filmOptions/$',views.filmOptions),
)