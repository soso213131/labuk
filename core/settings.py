import os
from pathlib import Path

# Побудова шляхів усередині проекту
BASE_DIR = Path(__file__).resolve().parent.parent

# Швидкі налаштування розробки
SECRET_KEY = 'django-insecure-q9#-64g!-czv!@309)d&!vx=(*+m81-wz#zat&*rax$j$fstmh'
DEBUG = True
ALLOWED_HOSTS = []

# Визначення додатків
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Твої додатки
    'web_app',
    'cart',
    'orders',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# База даних
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валідація паролів
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
]

# Інтернаціоналізація
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'Europe/Kyiv'
USE_I18N = True
USE_TZ = True

# Статичні файли (CSS, JavaScript)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Медіафайли (Зображення товарів)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Налаштування кошика
CART_SESSION_ID = 'cart'

# НАЛАШТУВАННЯ РЕАЛЬНОЇ ПОШТИ (Gmail SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Твої дані для авторизації
EMAIL_HOST_USER = 'nazar.onischuk@gimn14.lutsk.ua'
EMAIL_HOST_PASSWORD = 'pzlgrwfoqoaiyhfc' # Пароль додатка без пробілів

# Адреса, яка буде вказана як відправник
DEFAULT_FROM_EMAIL = 'Магазин Рибалка <nazar.onischuk@gimn14.lutsk.ua>'

LOGIN_REDIRECT_URL = 'home_page'
LOGOUT_REDIRECT_URL = 'home_page'

CART_SESSION_ID = 'cart'