from django.urls import path, include
from myapp import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile_view, name="profile"),
    path('social-auth', include('social_django.urls', namespace="social")),
    path("register",views.register_view, name="register"),
    path("new_user",views.new_user, name="new_user"),
    path("edit_user",views.edit_user, name="edit_user"),

    #path('accounts/', include('django.contrib.auth.urls')),   
    #path("", views.home, name="home"),  
]
