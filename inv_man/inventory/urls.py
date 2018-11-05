from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^(?P<inven_name>[0-9]+)/$', views.detail, name='detail'),
               # ex: /polls/5/results/
               url(r'^(?P<inven_name>[0-9]+)/results/$', views.create_comp, name='create_comp'),
               ]
