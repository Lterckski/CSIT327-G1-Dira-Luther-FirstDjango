from django.contrib import admin
from django.urls import path, include
from accounts.views import accounts_admin_index

urlpatterns = [
    path("admin/accounts/", admin.site.admin_view(accounts_admin_index), name="accounts_admin_index"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("dashboard.urls")),
]