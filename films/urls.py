from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static
from django.conf import settings
from films import views
from films.views import *
from films.models import Film

from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lafg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^search_form/(?P<option>\d+)/$', views.search_form, name='search_form'),
    #url(r'^top_rated/$', views.top_rated, name='top_rated'),
    url(r'^top_rated/$',ListView.as_view(
                                    queryset=Film.objects.filter(rate__gt=4, display=1),
                                    template_name="films/toprated.html" )), 
    url(r'^film_edit/$', views.film_edit, name='film_edit'),
    url(r'^seeFilmDetail/$', views.seeFilmDetail, name='seeFilmDetail'),
    url(r'^film_add/$', views.film_add, name='film_add'),
    url(r'^searchOptions/(?P<option>\d+)/$',views.searchOptions),
    url(r'^filmOptions/$',views.filmOptions),
    url(r'^filmUpdate/$',views.filmUpdate),
)