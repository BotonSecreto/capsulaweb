import os,json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bq8hi^xfy-cmq$7%rxax0cn4pb%ngj-17jir(ftvvz@2m-b#wz'

# ************Claves para reCAPTCHA: 127.0.0.1**************
RECAPTCHA_PUBLIC_KEY = '6LesznYlAAAAACRNhu0qz3m0rjsJukLiltum30BN'
RECAPTCHA_PRIVATE_KEY = '6LesznYlAAAAALw9f1lXzJiI2rZrJO0DgWFHDRZ1'
#  *********************************************

MESSAGE_STORAGE= "django.contrib.messages.storage.cookie.CookieStorage"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'ckeditor', #editor CKeditor de texto para páginas especiales
    'contact', #activar formulario contacto
    'about.apps.AboutConfig', #activar pagina nosotros y configuraciones de 'app'
    'social.apps.SocialConfig', #activar modelo "social"
    'catalogo.apps.CatalogoConfig', #activar modelo "catalogo" del home
    'captcha', #activar reCAPTCHA para formulario de contacto ---->>>> ¿NECESARIO?
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

ROOT_URLCONF = 'capsuladiscos.urls'

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
                'social.processors.ctx_dict',   # <====
            ],
        },
    },
]

WSGI_APPLICATION = 'capsuladiscos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Configurar los campos donde queramos mostrar el editor CKeditor(WYSIWYG)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['FontSize', 'Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink']
        ]
    }
}

# Email configuración invocando datos del archivo json
EMAIL_SETTING_FILE = os.path.join(BASE_DIR / "hocult",'email_setting.json')
with open(EMAIL_SETTING_FILE) as data_file:
    email_setting = json.load(data_file)

EMAIL_HOST = email_setting['EMAIL_HOST']
EMAIL_HOST_USER = email_setting['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_setting['EMAIL_HOST_PASSWORD']
EMAIL_PORT = email_setting['EMAIL_PORT']
EMAIL_USE_TLS = email_setting['EMAIL_USE_TLS']

