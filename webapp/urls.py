from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signupp/', views.signupp, name='signupp'),
	url(r'^signupd/', views.signupd, name='signupd'),
	url(r'^login/', views.login, name='login'),
]