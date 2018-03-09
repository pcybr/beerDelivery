from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^person/(?P<pk>\d+)$', views.getPerson, name = 'get_person'),
]