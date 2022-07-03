from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^hello/$', views.hello),
    re_path(r'^card/$', views.card),
    re_path(r'^random_cards$', views.random_cards),
    re_path(r'^welcome/$', views.welcome),
    re_path(r'^token_test/$',views.token_test),
    re_path(r'^form_test/$', views.form_test),
    re_path(r'^form_card/$', views.form_card),
    re_path(r'^login/$', views.login, name = "login"),

]