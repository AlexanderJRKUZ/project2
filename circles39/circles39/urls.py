
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('liked', views.liked, name='liked'),
    path('contacts', views.contacts, name='contacts'),
    path('account', views.account, name='account'),
    path('account/logout', views.logout, name='logout'),
    path('account/signup', views.signup, name='signup'),
    path('account/signup/sign-up', views.sign_up),
    path('account/login', views.login, name='login'),
    path('account/login/log-in', views.log_in),
    path('testfilter', views.testfilter, name='testfilter'),
    path('testfilter/test', views.test, name='test'),
    path('testfilter/filter', views.filter, name='filter'),
]

