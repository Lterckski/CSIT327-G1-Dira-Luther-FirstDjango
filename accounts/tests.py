from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class SignUpTests(TestCase):
    def test_signup_shows_success_message(self):
        response = self.client.post(reverse("signup"), {
            "username": "juan",
            "email": "juan@example.com",
            "first_name": "Juan",
            "last_name": "Dela Cruz",
            "course": "BSIT",
            "password1": "CampusPass123!",
            "password2": "CampusPass123!",
        }, follow=True)
        self.assertRedirects(response, reverse("login"))
        self.assertContains(response, "Account created for juan")
        self.assertContains(response, "alert-success")


class ProfileTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="maria", password="CampusPass123!")
        self.other = CustomUser.objects.create_user(
            username="pedro", password="CampusPass123!", course="BSCS")

    def test_profile_requires_login(self):
        response = self.client.get(reverse("profile"))
        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('profile')}")

    def test_user_edits_only_own_profile(self):
        self.client.login(username="maria", password="CampusPass123!")
        response = self.client.post(reverse("profile"), {
            "first_name": "Maria",
            "last_name": "Santos",
            "email": "maria@example.com",
            "course": "BSIT",
        }, follow=True)
        self.assertContains(response, "Your profile has been updated.")
        self.user.refresh_from_db()
        self.other.refresh_from_db()
        self.assertEqual(self.user.course, "BSIT")
        self.assertEqual(self.other.course, "BSCS")

    def test_user_cannot_change_own_role(self):
        self.client.login(username="maria", password="CampusPass123!")
        self.client.post(reverse("profile"), {
            "first_name": "Maria",
            "course": "BSIT",
            "role": CustomUser.Role.ADMIN,
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.role, CustomUser.Role.STUDENT)

    def test_forms_include_csrf_token(self):
        for name in ("signup", "login"):
            self.assertContains(
                self.client.get(reverse(name)), "csrfmiddlewaretoken")
