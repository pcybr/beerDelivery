from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^index/$', views.index, name = 'index'),
	url(r'^person/(?P<pk>\d+)$', views.getPerson, name = 'get_person'),
	url(r'^order/(?P<pk>\d+)$', views.getOrder, name = 'get_order'),
	url(r'^trip/(?P<pk>\d+)$', views.getTrip, name = 'get_trip'),
	url(r'^beer/(?P<pk>\d+)$', views.getBeer, name = 'get_beer'),
	url(r'^store/(?P<pk>\d+)$', views.getStore, name = 'get_store'),

	url(r'^person/all', views.getAllPeople, name = 'get_all_people'),
	url(r'^beer/all', views.getAllBeers, name = 'get_all_beers'),
	url(r'^store/all', views.getAllStores, name = 'get_all_stores'),
	url(r'^trip/all', views.getAllTrips, name = 'get_all_trips'),
	url(r'^order/all', views.getAllOrders, name = 'get_all_orders'),

	url(r'^login/', views.login, name = 'login'),
	url(r'^signup/', views.signup, name = 'signup'),
	url(r'^createTrip/', views.createTrip, name = 'createTrip'),
	url(r'^createOrder/', views.createOrder, name = 'createOrder'),
	url(r'^logout/', views.logout, name = 'logout'),
	url(r'^checkAuth/', views.checkAuth, name = 'check_auth'),

]
