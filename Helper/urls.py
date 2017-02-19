from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SystemList.as_view(), name='main'),
    url(r'system(?P<sys_id>[0-9]+)/$', views.ElementList.as_view(), name='element')
]
