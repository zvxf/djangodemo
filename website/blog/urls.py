from django.urls import re_path, path
from blog.views import *
from django.views.static import serve
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    re_path(r'^$', index, name='index'),
    re_path(r'^login/$', log_in, name='login'),
    re_path(r'^logout/$', log_out, name='logout'),
    re_path(r'^reg/$', reg, name='reg'),
    path('art/<int:id>/', art, name='art'),
    re_path(r'^post/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})(?P<id>[0-9])/$', post, name='post'),

]
