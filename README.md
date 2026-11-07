# CampusConnect – First Django Application

**Name:** Luther Derrick Dira
**Section:** G1
**Course:** CSIT327 – Information Management 2

CampusConnect is a small Django app with sign-up, login, a dashboard, and a profile page, styled with Bootstrap 5 (CDN).

## Features

- **Sign-up and Login** using a custom user model (`accounts.CustomUser`)
- **Profile page** (`/accounts/profile/`) built with a class-based `UpdateView`
  - Requires login (`LoginRequiredMixin`)
  - Always loads the logged-in user (`get_object` returns `request.user`), so no one can open or edit another user's profile
  - Role is not editable, so users cannot promote themselves to admin
- **Success messages** with Django's messages framework, shown as Bootstrap alerts after sign-up and profile updates
- **Shared `base.html`** with the Bootstrap 5 CDN links and a navbar, extended by every page
- **CSRF protection** on every form

## How to Run

1. Clone the repository and go into the folder:
   ```bash
   git clone https://github.com/Lterckski/CSIT327-G1-Dira-Luther-FirstDjango.git
   cd CSIT327-G1-Dira-Luther-FirstDjango
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply the migrations:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Create an admin account:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```
7. Open http://127.0.0.1:8000/accounts/signup/ to create an account.

## Running the Tests

```bash
python manage.py test
```

## Main Pages

| Page        | URL                     |
|-------------|-------------------------|
| Sign up     | `/accounts/signup/`     |
| Log in      | `/accounts/login/`      |
| Dashboard   | `/`                     |
| Profile     | `/accounts/profile/`    |
| Admin panel | `/admin-panel/`         |
