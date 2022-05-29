from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homePage', views.index, name='index'),
    path('adoptPage', views.adoptPage, name='adoptPage'),
    path('wantoAdopt', views.wantoAdopt, name='wantoAdopt')
]