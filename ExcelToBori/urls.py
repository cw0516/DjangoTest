from django.conf.urls import url
from bori import views

urlpatterns = [
    url(r'^bori', views.bori_controller),
]
