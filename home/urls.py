from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    # path('collection',views.collection.as_view(),name="collection"),
]
