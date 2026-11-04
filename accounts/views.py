from django.contrib import admin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

def accounts_admin_index(request):
    # Show "Authentication and Authorization" (Groups) below Accounts on /admin/accounts/
    app_list = admin.site.get_app_list(request, "accounts") + admin.site.get_app_list(request, "auth")
    return admin.site.app_index(request, "accounts", extra_context={"app_list": app_list})
