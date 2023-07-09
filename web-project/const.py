## Discord App Credential for login in api editor localhost:8000/data/ (api.py)
DISCORD_CLIENT_ID = '######'
DISCORD_CLIENT_SECRET = '######'
DISCORD_NOTIF_ROLE_ID = '######'
DISCORD_ERROR_ROLE_ID = '######'
DEV_MODE = True
DEBUG_STATS = False ## if True : get the print() of all calculation function in models.py and be able to access update views for all users
c_CSRF_FAILURE_VIEW = 'calculator.views_wiki.csrf_failure'
c_CSRF_USE_SESSION = True
c_CSRF_COOKIE_SECURE = True
c_CSRF_COOKIE_DOMAIN = [""]
c_CSRF_TRUSTED_ORIGINS = [""]
c_ALLOWED_HOSTS = [""]
# Follow the steps below to generate a Django secret key:

# Access the Python Interactive Shell
# Import get_random_secret_key() from django.core.management.utils.
# Generate the Secret Key in the Terminal using the get_random_secret_key() function
# Copy and Paste the Key into your SECRET_KEY variable in the const.py
c_SECRET_KEY = '##########'

ADMIN_CREDENTIAL = {
    "#####":"#####"
}

if DEV_MODE:
    c_hostname = "http://127.0.0.1:8000"
    WEBHOOK_URL = "https://discord.com/api/webhooks/###########/#################################"
    ADMIN_LOG_WEBHOOK_URL = "https://discord.com/api/webhooks/###########/#################################"
    c_DEBUG = True
    c_DATABASES = {
        'default': {
            'ENGINE': '######',
            'NAME': '#####',
            'USER': '#####',
            'HOST': 'localhost',
            'PASSWORD': '#####',
            'PORT': '#####',
        }
    }
else:
    c_hostname = "https://stats.wiki-archero.com"
    WEBHOOK_URL = "https://discord.com/api/webhooks/###########/#################################"
    ADMIN_LOG_WEBHOOK_URL = "https://discord.com/api/webhooks/###########/#################################"
    c_DEBUG = False
    c_DATABASES = {
        'default': {
            'ENGINE': '######',
            'NAME': '#####',
            'USER': '#####',
            'HOST': 'db',
            'PASSWORD': '####',
            'PORT': '#####',
        }
    }