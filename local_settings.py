MONGODB_URI = "mongodb://221.130.162.44:27017"
#MONGODB_URI = "mongodb://root:happy@127.0.0.1:27017"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'carpenter',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
 
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
       }
 
}
