from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from users import views
from users.views import *

from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lafg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^search_form/(?P<option>\d+)/$', views.search_form, name='search_form'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_update_info/$', views.user_update_info, name='user_update_info'),
    
)