from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SystemList.as_view(), name='main'),
    url(r'(?P<sys_slug>[-\w]+)/$', views.SystemDetail.as_view(), name='system-detail'),
    url(r'(?P<sys_slug>[-\w]+)/(?P<elem_slug>[-\w]+)/$', views.ElementDetail.as_view(), name='element-detail'),
]

#id(?P<elem_id>[0-9]+)
"""url(r'(?P<sys_slug>[-\w]+)/(?P<elem_slug>[-\w]+)/$',
views.ElementDetail.as_view(), name = 'element-detail' """