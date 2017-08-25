echo ***Running python manage.py collectstatic***
python manage.py collectstatic

echo ***Running python manage.py assets build***
python manage.py assets build

echo ***Running python manage.py runserver***
python manage.py runserver
