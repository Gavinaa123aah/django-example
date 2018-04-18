from django.conf.urls import url

from . import views

urlpatterns = [
    url('view1/', views.index, name='index'),
]