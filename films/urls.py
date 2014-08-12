from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, FormView
from django.conf.urls.static import static
from django.conf import settings
from films import views
from films.views import *
from films.models import Film
from films.forms import FilmForm
#from films.views.cbv.ListView import Film_TopRatedListView

from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lafg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^search_form/(?P<option>\d+)/$', views.search_form, name='search_form'),
    #url(r'^top_rated/$', views.top_rated, name='top_rated'),
    url(r'^top_rated/$',Film_TopRatedList.as_view(), name="top_rated"), 
    url(r'^film_edit/$', views.film_edit, name='film_edit'),
    url(r'^seeFilmDetail/$', views.seeFilmDetail, name='seeFilmDetail'),
    url(r'^film_add/$', FilmAddView.as_view(), name='film_add'),
    #url(r'^film_add/$', FilmAddCreateView , name='filmAddCreateView'),
    url(r'^searchOptions/(?P<option>\d+)/$',views.searchOptions),
    url(r'^filmOptions/$',views.filmOptions),
    url(r'^filmUpdate/$',views.filmUpdate),
)