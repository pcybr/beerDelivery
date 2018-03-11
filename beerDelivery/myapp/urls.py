from django.conf.urls import url
from . import views


# Send the pk value of a model in a POST when trying to submit a model as a field of another model
# i.e., when making an Order instance, send an integer pk value of an existing person and beer for the 'buyer' and 'item' fields

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
  
	url(r'^beerdelivery/', views.index, name = 'index'),
	url(r'^api/v1/person/(?P<pk>\d+)$', views.ApiPersonGetView, name='person_get'),
	url(r'^api/v1/person/create', views.ApiCreatePerson, name='person_create'),
	url(r'^api/v1/person/(?P<pk>\d+)/delete$', views.ApiPersonDeleteView, name='person_delete'),
	url(r'^api/v1/person/(?P<pk>\d+)/update$', views.ApiUpdatePerson, name='person_update'),
	url(r'^api/v1/person/all$', views.ApiAllPersons, name='person_all'),



	url(r'^api/v1/beer/(?P<pk>\d+)$', views.ApiBeerGetView, name='beer_get'),
	url(r'^api/v1/beer/create', views.ApiCreateBeer, name='beer_create'),
	url(r'^api/v1/beer/(?P<pk>\d+)/delete$', views.ApiBeerDeleteView, name='beer_delete'),
	url(r'^api/v1/beer/(?P<pk>\d+)/update$', views.ApiUpdateBeer, name='beer_update'),


	url(r'^api/v1/store/(?P<pk>\d+)$', views.ApiStoreGetView, name='store_get'),
	url(r'^api/v1/store/create', views.ApiCreateStore, name='store_create'),
	url(r'^api/v1/store/(?P<pk>\d+)/delete$', views.ApiStoreDeleteView, name='store_delete'),
	url(r'^api/v1/store/(?P<pk>\d+)/update$', views.ApiUpdateStore, name='store_update'),


	url(r'^api/v1/trip/(?P<pk>\d+)$', views.ApiTripGetView, name='trip_get'),
	url(r'^api/v1/trip/create', views.ApiCreateTrip, name='trip_create'),
	url(r'^api/v1/trip/(?P<pk>\d+)/delete$', views.ApiTripDeleteView, name='trip_delete'),
	url(r'^api/v1/trip/(?P<pk>\d+)/update$', views.ApiUpdateTrip, name='trip_update'),
	

	url(r'^api/v1/order/(?P<pk>\d+)$', views.ApiOrderGetView, name='order_get'),
	url(r'^api/v1/order/create', views.ApiCreateOrder, name='order_create'),
	url(r'^api/v1/order/(?P<pk>\d+)/delete$', views.ApiOrderDeleteView, name='order_delete'),
	url(r'^api/v1/order/(?P<pk>\d+)/update$', views.ApiUpdateOrder, name='order_update'),


]
