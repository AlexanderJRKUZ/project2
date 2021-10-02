from django.conf.urls.static import static
from django.conf import settings 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('liked', views.liked, name='liked'),
    path('contacts', views.contacts, name='contacts'),
    path('account', views.account, name='account'),
    path('account/logout', views.logout, name='logout'),
    path('account/signup', views.signup, name='signup'),
    path('account/signup/parent', views.signup_parent, name='signup_parent'),
    path('account/signup/sign-up-parent', views.sign_up_parent),
    path('account/signup/child', views.signup_child, name='signup_child'),
    path('account/signup/sign-up-child', views.sign_up_child),
    path('account/login', views.login, name='login'),
    path('account/log-in', views.log_in),
    path('testfilter', views.testfilter, name='testfilter'),
    path('testfilter/test', views.test, name='test'),
    path('testfilter/filter', views.filter, name='filter'),
]

