from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, ProfileForm

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Account created for %(username)s. You can now log in."

class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = ProfileForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("profile")
    success_message = "Your profile has been updated."

    def get_object(self, queryset=None):
        # Users can only ever edit their own profile
        return self.request.user

def accounts_admin_index(request):
    # Show "Authentication and Authorization" (Groups) below Accounts on /admin/accounts/
    app_list = admin.site.get_app_list(request, "accounts") + admin.site.get_app_list(request, "auth")
    return admin.site.app_index(request, "accounts", extra_context={"app_list": app_list})
