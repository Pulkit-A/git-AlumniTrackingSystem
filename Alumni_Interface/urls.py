from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('alumniLogin/', LoginView.as_view(), name="login_"),
    path('', views.home_view, name="home"),
    path('Login/Signup/', views.register),
    path('alumniDetails/', views.info_input),
    path('dashboard/', views.dashboard_view),
    path('profile/', views.profile_view, name="profile"),
    path('profile/edit/', views.info_edit),
    path('logout/', views.logout, name="logout")
]