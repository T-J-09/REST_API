from django.conf.urls import url
from Api_Assign import views

urlpatterns = [
    url(r'^api/movies/', views.summary),
    url(r'^api/movies/(?P<pk>[0-9]+)$', views.details),

]
