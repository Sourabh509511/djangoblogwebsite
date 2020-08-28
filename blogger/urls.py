from django.urls import path
from . import views







urlpatterns = [
    path('', views.home,name="home"),
    path('blogger/<str:slug>', views.blogger,name="blogger"),
    path('comment', views.postcomment,name="comment"),
]
