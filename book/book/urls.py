"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	# url(r'^$', 'bname.views.index'),
	url(r'^$','bname.views.search_form'),
	url(r'^search/$','bname.views.search'),
	url(r'^book/(?P<bookISBN>\d*)','bname.views.book'),
	url(r'^Author/(?P<bookAuthorID>\d*)','bname.views.Autho'),
	url(r'^delete/(?P<bookISBN>\d*)','bname.views.delete'),
	url(r'^change/(?P<bookISBN>\d*)','bname.views.change'),
	url(r'^update/(?P<bookISBN>\d*)','bname.views.update'),
	url(r'^addauthor/$','bname.views.addauthor'),
	url(r'^addbook/$','bname.views.addbook'),
	url(r'^adb/$','bname.views.adb'),
	url(r'^ada/$','bname.views.ada'),
	url(r'^showauthor/$','bname.views.showauthor'),
	url(r'^showbook/$','bname.views.showbook'),
]
