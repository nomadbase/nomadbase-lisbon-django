from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<question_id>[a-zA-Z]+)/$', views.index, name='index'),
#    url(r'^home|home/', views.index, name='index'),
#    url(r'^participate|participate/', views.index, name='index'),
#    url(r'^activity|activity/', views.index, name='index'),
#    url(r'^values|values/', views.index, name='index'),
#    url(r'^contact|contact/', views.index, name='index'),
#    url(r'^come|come/', views.index, name='index'),
#    url(r'^$', views.index, name='index'),
]
