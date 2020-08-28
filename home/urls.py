from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome,name="index"),
    path('home/contact', views.contact,name="contact"),
    path('home/about', views.about,name="about"),
    path('home/search', views.search,name="search"),
    path('auth', views.authentication,name="authenticate"),
    path('logout', views.logoutView,name="logout"),
    path('login', views.loginView,name="login"),
    # path('login', views.LoginClassView.as_view(),name="login"),
]
