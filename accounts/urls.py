from django.contrib.auth.views import LoginView
from django.urls import path
from .forms import LoginForm
from .views import SignUpView, ProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(),
         name="signup"),
    path("login/", LoginView.as_view(authentication_form=LoginForm),
         name="login"),
    path("profile/", ProfileView.as_view(),
         name="profile"),
]
