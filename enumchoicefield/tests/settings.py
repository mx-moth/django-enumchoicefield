import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite://:memory:'),
}

INSTALLED_APPS = ['enumchoicefield', 'enumchoicefield.tests']

SECRET_KEY = 'not a secret'

DEBUG = True
