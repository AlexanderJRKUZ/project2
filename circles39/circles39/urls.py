from django.conf.urls.static import static
from django.conf import settings 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('liked', views.liked, name='liked'),
    path('contacts', views.contacts, name='contacts'),
    path('account', views.account, name='account'),
    path('registration', views.reg, name='reg'),
    path('testfilter', views.testfilter, name='testfilter'),
    path('testfilter/test', views.test, name='test'),
    path('testfilter/filter', views.filter, name='filter'),
]

