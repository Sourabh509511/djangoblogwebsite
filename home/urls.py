from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome.as_view(),name="index"),
    path('home/contact', views.contact.as_view(),name="contact"),
    path('home/about', views.about.as_view(),name="about"),
    path('home/search', views.search.as_view(),name="search"),
    path('auth', views.authentication.as_view(),name="authenticate"),
    path('logout', views.logoutView.as_view(),name="logout"),
    path('login', views.loginView.as_view(),name="login"),
    # path('login', views.LoginClassView.as_view(),name="login"),
]
