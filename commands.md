# Commands

django-admin startproject drfecommerce .

python manage.py runserver

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

python manage.py spectacular --file schema.yml

pip freeze > requirements.txt

isort .

coverage run -m pytest

pytest --cov

coverage html
# Packages
Django
djangorestframework
psycopg2-binary
python-dotenv
pytest
pytest-django
black
django-mptt
drf-spectacular
coverage
pytest-cov
pytest-factoryboy