from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^grid-tiles/', views.grid, name='grid'),
    url(r'^blog/', views.blog, name='blog')
]