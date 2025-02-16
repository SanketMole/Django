`Django`: Django is a high level python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.   

**Features**: 
1. `Ridiculously fast`: Django was designed to help developers take applications from concepts to completion as quickly as possible. 
2. `Fully Loaded`: Django includes dozens of extras you can use to handle common web development tasks. Django takes care of user authentication, content administration, site maps, RSS feeds and many more tasks. 
3. `Reassuringly secure`: Django takes security seriously and helps developers avoid many common security mistakes, such as SQL injection, cross-site scripting, cross-site request forgery and clickjacking. Its user authentication system provides a secure way to manage user accounts and passwords. 
4. `Exceedingly scalable`: Some of the busiest sites on the planet uses Django's ability to quickly and flexibly scale to meet the heaviest traffic demands. 
5. `Incredibly versatile`: Companies, organizations and governments have used Django to build all sorts of things- from content management systems to social networks to scientific computing platforms. 


Professionals don't download Django directly, rather they create a virtual environment.    

**Steps**: 
1. Install `uv` instead of pip. *uv* is an extremely fast python package installer and resolver, written in Rust.   
To install *uv* write `pip install uv`. 
2. Create virtual environment using `uv venv` command.   
Now we have to run activation script which we got after installing venv. 
3. Navigate to activate folder. Run `.venv\Scripts\activate`.    
Now you are in *virtual environment*, run `deactivate` to simply deactivate virtual environment.   

Note: Hereonwards if any need to download any library, run `uv pip install flask or <name_of_library>`.   

4. Now download 'Django'. Run `uv pip install Django`. 
5. Create a Django project on the running virtual environment. 
'django-admin' which is a Django cmd which we get after we download Django.  
'startproject' is a sub-cmd of Django used to create project, we run this cmd only once, after this we will create small-small apps.   
Run `django-admin startproject newDjango`.   
6. Go to the project folder `cd newDjango` and also run `ls` to know files.   
7. To run project `python manage.py runserver`. Ignore errors they are encountered initially. 

*Django files Exploration*: 
- `manage.py`: It is a starting point file. It will set environment variables. In production 'manage.py' invokes the whole system. Many options are available in this file.     
**Note**: Manage file is at *project-level*. Levels are important in Django. Inside first parent 'newDjango' folder comes the project-level or root-level where we have another 'newDjango' folder, 'db.sqlite3' file and 'manage.py' file. Then inside 'newDjango', comes the app-level.     
- `db.sqlite3`: This is a default Database file of Django. Using one-two cmd, we can shift to any DBMS i.e. PostgreSQL, SQL, etc. 
- `_pycache_`: It is cache folder which we see in every python project. 
- `settings.py`: All configuration of Django are written here. We come here very rarely.
- `urls.py`: Routing file (i.e. where you can navigate, what changes occurs when we navigate and all such operations). 'admin' is by default in urls. 
- `views.py`: Defines controllers, all funcitonalities, buissness logics are controlled in 'views.py'. 
- `models.py`: Here we store all DataBase models. 

**In a typical Django application**:-
1. We hit 'url.py' file, governs which route will handle the application. Then all control goes to 'views.py'. 
2. In 'views.py' we have buissness logic and here we return either HTML file or any similar file. 
3. Then comes 'models.py' where our database is designed. 