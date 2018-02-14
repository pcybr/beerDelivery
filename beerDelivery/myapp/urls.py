from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^beerdelivery/', views.index, name = 'index'),

    url(r'^api/v1/person/(?P<pk>\d+)$', views.ApiPersonGetView, name='person_get'),
    url(r'^api/v1/person/create/', views.ApiCreatePerson, name='person_create'),
    url(r'^api/v1/person/(?P<pk>\d+)$)', views.ApiPersonDeleteView, name='person_delete'),




    url(r'^api/v1/beer/(?P<pk>\d+)$', views.ApiBeerGetView, name='beer_get'),



    url(r'^api/v1/store/(?P<pk>\d+)$', views.ApiStoreGetView, name='store_get'),
   


    url(r'^api/v1/trip/(?P<pk>\d+)$', views.ApiTripGetView, name='trip_get'),
   


   url(r'^api/v1/order/(?P<pk>\d+)$', views.ApiOrderGetView, name='order_get'),


    #url(r'^api/v1/person/(?P<pk>[-\w]+)/$', views.ApiPersonGetView, name='person_get'),

    
]
