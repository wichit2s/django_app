import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

mongo = {
    'ENGINE': 'djongo',
    'NAME': 'mysitedb',
    #'HOST': '127.0.0.1',
    'HOST': 'db', # when run with docker-compose up
    'PORT': 27017,
}
mysql = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'mysitedb',
    #'HOST': '127.0.0.1',
    'HOST': 'db', # when run with docker-compose up
    'PORT': 3306,
}
postgres = {
    'ENGINE': 'django.db.backends.postgresql',
    #'HOST': '127.0.0.1', 
    'HOST': 'db', # when run with docker-compose up
    'PORT': 5432,
}
sqlite3 = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
