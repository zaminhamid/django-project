from django.conf.urls import url
from . import views

urlpatterns=[
	#home page
	url(r'^$',views.index,name='index'),
	url(r'^topics/$',views.topics,name='topics'),
	#details of a single topic
	url(r'^topics/(?P<topic_id>\d+)$',views.topic,name='topic'),
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	
	
]
