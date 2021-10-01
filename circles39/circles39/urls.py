from django.conf.urls.static import static
from django.conf import settings 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration', views.reg, name='reg'),
    path('testfilter', views.testfilter, name='testfilter'),
    path('testfilter/test', views.test, name='test'),
    path('testfilter/filter', views.filter, name='filter'),
]

