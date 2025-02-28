## How to install Tailwind in Django?
To install Tailwind in a Django project, you can follow these steps:
1. Firstly activate the environment by navigating to root folder and then '.venv/bin/activate'. 
2. Run `uv pip install django-tailwind`. 
3. We want Hot-Reloading(i.e. as we make changes it should directly render), for that we first install 'pip'. Use 
either `python -m ensurepip --upgrade` or `python -m pip install --upgrade pip` or sometimes if error occurs run both. 
4. Now as we have installed pip, we don't need to use 'uv' from now onwards in any cmd. Thus, for Hot-Reloading
run `pip install 'django-tailwind[reload]'`. 
5. Add app in setting.py, naming as 'tailwind'. Run `python manage.py tailwind init` in root folder. Then name your app (mostly 'theme'). Thus add another app in settings.py 'theme'. 
6. Below app array, create a new array, `TAILWIND_APP_NAME = 'theme'` and also `INTERNAL_IPS=['127.0.0.1']`. 
7. Now install Tailwind, `python manage.py tailwind install`. 
8. Import tailwind tags in our template folder's layout.html, `{% load static tailwind_tags %}` and below link tag add `{ % tailwind_css %}`. 
9. We can write tailwind in layout.html but not in other html file (index.html). For that case, create a new terminal and activate `.venv/bin/activate`. Then run `python manage.py tailwind start`. Now tailwind is continuously running in background. If you're on production grade, `python manage.py tailwind build`. 


Probable errors which can be encountered, for safety purpose:-
1. In settings.py `NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'` to check path run `where npm` in windows terminal. You can write path as `NPM_BIN_PATH = r"path"`. 
2. Add `'django_browser_reload'` in apps of settings.py. Also add middleware `'django_browser_reload.middleware.BrowserReloadMiddleware'`. 
3. In urls.py in urlpatterns `path("__reload__/", include("django_browser_reload.urls")),`. Always put this path in last of urlpatterns, this is the path which auto-reloads, as it is a heavy path we should always put this in last. 


Restart both terminals once done all configs, `python manage.py runserver` and `python manage.py tailwind start`. 



## Tackling most occuring warninig while running server
To avoid the warning of '18 unapplied migrations', 
run `python manage.py migrate`


## How to create super user
Run `python manage.py createsuperuser` - Enter user name (Eg: sanket) - Email address is not compulsary - password. 
(User: sanket, pass: SSM@123456)

## To change password
`python manage.py changepassword hitesh`
