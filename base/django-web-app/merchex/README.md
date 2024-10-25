### django ###
* terminal commande
    * initialisation
        * python -m venv env -> create environment
        * pip install django -> install django
        * pip freeze > requirements.txt -> create a file with all dependency
        * django-admin startproject projectName . -> initialize the project
        * python manage.py runserver -> run python server

    * DB
        * migration
            * python manage.py makemigrations -> create migration
            * python manage.py migrate -> migrate the DB (sqlite per default)
        * migrations error
          * python manage.py showmigrations -> see migration list
          * python manage.py migrate migrationName -> run a previous migration
          * rm appName/migrations/migrationName -> delete migration
          * python manage.py makemigrations --merge -> in case of migrations with the same number

        * generate data in BD
            * python manage.py shell
            * from appName.models import Model
            * model = Model()     \
            * model.name = "abc"  / ===>> model = Model.objects.create(name='Foo Fighters')
            * model.save()
            * model  => see the model id
            * Model.objects.count()
            * Model.objects.all()
            * ctrl + d or quit() -> to quit shell

        * CRUD
          * python manage.py createsuperuser ===>> create a super user

* app
    * python manage.py startapp appName -> create an new app in the project to structured code in several app
    * add the app name in projectName/settings.py in the INSTALLED_APPS list
    * in projectName/urls.py import the views from the app and add the URL in the list
    * 