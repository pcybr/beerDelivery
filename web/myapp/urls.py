from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^person/(?P<pk>\d+)$', views.getPerson, name = 'get_person'),
	url(r'^order/(?P<pk>\d+)$', views.getOrder, name = 'get_order'),
	url(r'^trip/(?P<pk>\d+)$', views.getTrip, name = 'get_trip'),
]