from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$',views.index,name = 'index'),
		url(r'^dashboard',views.index1,name='index1'),
                url(r'^notifications',views.index2,name='index2'),
		url(r'^table',views.index3,name = 'index3'),
		url(r'^template',views.index4,name = 'index4'),
		url(r'^user',views.index5,name = 'index5')
		]
