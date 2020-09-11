from django.urls import path
from . import views







urlpatterns = [
    path('', views.home,name="home"),
    path('blogger/<str:slug>', views.blogger.as_view(),name="blogger"),
    path('comment', views.postcomment.as_view(),name="comment"),
]
