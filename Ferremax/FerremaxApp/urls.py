from django.urls import path, include
from . import views


urlpatterns=[

    path('', views.index, name='index'),

    path('store', views.store, name='store'),

    path('login', views.login, name='login'),

    path('register', views.login, name='register'),
]