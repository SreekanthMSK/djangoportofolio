from django.urls import path

from . import views
from myportfolio import views as adminview

urlpatterns = [
    # path('', views.index, name='index'),
    path('', adminview.index.as_view(), name='index'),
    path('',views.download_file,name='download'),
    path('readmore',adminview.readmore.as_view(),name='readmore'),
]