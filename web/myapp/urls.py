from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^person/(?P<pk>\d+)$', views.getPerson, name = 'get_person'),
	url(r'^order/(?P<pk>\d+)$', views.getOrder, name = 'get_order'),
	url(r'^trip/(?P<pk>\d+)$', views.getTrip, name = 'get_trip'),
	url(r'^beer/(?P<pk>\d+)$', views.getBeer, name = 'get_beer'),
	url(r'^store/(?P<pk>\d+)$', views.getStore, name = 'get_store'),

	url(r'^people/', views.getAllPeople, name = 'all_people'),
	url(r'^beers/', views.getAllBeers, name = 'all_beers'),
	url(r'^stores/', views.getAllStores, name = 'all_stores'),
	url(r'^trips/', views.getMyTrips, name = 'my_trips'),
	url(r'^activetrips/', views.getActiveTrips, name = 'active_trips'),
	url(r'^orders/', views.getAllOrders, name = 'all_orders'),
	url(r'^myorders/', views.getMyOrders, name = 'my_orders'),

	url(r'^login/', views.login, name = 'login'),
	url(r'^signup/', views.signup, name = 'signup'),
	url(r'^logout/', views.logout, name = 'logout'),

	url(r'^trip/create/', views.createTrip, name = 'createTrip'),
	url(r'^order/create/', views.createOrder, name = 'createOrder'),

	url(r'^trip/(?P<pk>\d+)/endTrip$', views.EndTrip, name = 'end_trip'),


]