from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signupp/', views.signupp, name='signupp'),
	url(r'^signupd/', views.signupd, name='signupd'),
	url(r'^login_view/', views.login_view, name='login_view'),
	url(r'^userhome/', views.userhome, name='userhome'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
]