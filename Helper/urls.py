from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SystemList.as_view(), name='main'),
    url(r'^helper/(?P<pk>[0-9]+)/$', views.SystemDetail.as_view(), name='element')
]
