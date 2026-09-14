# Cebu Survival Guide

A Django project using **vertical slicing architecture**: each screen is a
fully self-contained Django app (its own views, urls, forms, and templates),
rather than grouping code by technical layer.

## Vertical slices (apps)

```
home/                      Home Screen slice
    views.py                 home() view
    urls.py                  app_name = 'home'
    templates/home/
        home.html             "HOME SCREEN" marker + landing content

login/                     Login slice (also owns logout, same auth-session concern)
    views.py                  CebuLoginView, CebuLogoutView
    urls.py                   app_name = 'login'
    templates/login/
        login.html

register/                  Register slice
    forms.py                  RegisterForm (extends UserCreationForm)
    views.py                  register() view
    urls.py                   app_name = 'register'
    templates/register/
        register.html
```

Each app is independent and only depends on Django itself plus the shared,
cross-cutting shell below — it does not import from the other two apps.

## Shared / cross-cutting (not a slice)

```
templates/base.html         Layout + top navigation bar, used by all screens
static/css/style.css        Shared color palette, buttons, forms
cebu_survival_guide/         Project settings + root urls.py (mounts each slice)
```

## Navigation flow

```
Home ("/")
 ├─ Login button (top right)    -> /login/
 │                                   -> "Register here" link -> /register/
 │                                   -> on success -> redirect to Home (logged in)
 └─ Register button (top right) -> /register/
                                     -> "Log in here" link -> /login/
                                     -> on success -> auto-login -> redirect to Home

Home (logged in)
 └─ Logout button (top right)   -> /login/logout/ -> redirect to Home (logged out)
```

URL names, for use in templates/redirects:
- `home:home` -> `/`
- `login:login` -> `/login/`
- `login:logout` -> `/login/logout/`
- `register:register` -> `/register/`

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

This runs on a local `db.sqlite3` file. Run `python manage.py migrate`
any time you pull a fresh copy of this project without a database file —
it creates `db.sqlite3` and builds the tables Login/Register need
(including `auth_user`).

## Notes

- The Home Screen (`/`) is the first page visitors see.
- The logo in the top left is a placeholder ("Logo Here") — swap
  `.logo-placeholder` in `templates/base.html` for a real image later.
- To add a fourth screen as its own vertical slice, run
  `python manage.py startapp <name>`, add it to `INSTALLED_APPS`, give it its
  own `templates/<name>/` folder, and mount its `urls.py` in the project's
  root `urls.py` — no changes needed to the other slices.
