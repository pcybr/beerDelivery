from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^beerdelivery/', views.index, name = 'index'),
    url(r'^api/v1/person/(?P<pk>[-\w]+)/$', views.ApiPersonGetView, name='person_get'),
    url(r'^api/v1/beer/(?P<pk>[-\w]+)/$', views.ApiBeerGetView, name='beer_get'),
    url(r'^api/v1/store/(?P<pk>[-\w]+)/$', views.ApiStoreGetView, name='store_get'),
    url(r'^api/v1/trip/(?P<pk>[-\w]+)/$', views.ApiTripGetView, name='trip_get'),
    url(r'^api/v1/order/(?P<pk>[-\w]+)/$', views.ApiOrderGetView, name='order_get'),


]
