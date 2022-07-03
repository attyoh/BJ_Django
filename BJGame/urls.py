from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^game/$',views.game, name = 'game'),
    re_path(r'^howto/$', views.howto),
]