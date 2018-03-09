from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^person/(?P<pk>\d+)$', views.getPerson, name = 'get_person'),
	url(r'^beer/(?P<pk>\d+)$', views.getBeer, name = 'get_beer'),
	url(r'^store/(?P<pk>\d+)$', views.getStore, name = 'get_store'),
]