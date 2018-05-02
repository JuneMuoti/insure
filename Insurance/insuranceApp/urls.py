from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),

]
