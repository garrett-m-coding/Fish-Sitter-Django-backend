# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-2#se2w2t^20h%7g6_6+(zztxlmz#99f*r(dgsri7@ip_8zov@'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'fish_sitter_database',
        'USER': 'root',
        'PASSWORD': 'oregoN2030!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
