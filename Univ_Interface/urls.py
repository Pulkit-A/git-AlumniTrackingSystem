from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('Login/', LoginView.as_view(), name="login_"),
    path('Login/Signup/', views.register),
    path('UnivDetails/', views.info_input),
    path('Login/dashboard/', views.dashboard_view),
    path('eventadd/', views.add_event),
    path('dashboard/', views.dashboard_view, name="event"),
    path('alumni/', views.alumni_display),
    path('profile/', views.profile_view, name="profile"),
    path('profile/edit/', views.info_edit),
    path('logout/', views.logout, name="logout")
]