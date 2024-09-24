import os
from dotenv import load_dotenv

load_dotenv()

# Global configuration variables
DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
DISCORD_NOTIF_ROLE_ID = os.getenv("DISCORD_NOTIF_ROLE_ID")
DISCORD_ERROR_ROLE_ID = os.getenv("DISCORD_ERROR_ROLE_ID")
DISCORD_CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
ADMIN_LOG_WEBHOOK_URL = os.getenv("ADMIN_LOG_WEBHOOK_URL")
DEV_MODE = os.getenv("DEV_MODE", False).lower() in ('true', '1', 't')
## if DEBUG_STATS=True : get the print() of all calculation function in models.py and be able to access update views for all users
DEBUG_STATS = os.getenv("DEBUG_STATS", False).lower() in ('true', '1', 't')
ADMIN_CREDENTIAL = {}

# If you want to have analytics locally, you'll need to install Matomo on your server and change the following variables
MATOMO_TOKEN_VIEW_ACCESS = os.getenv("MATOMO_TOKEN_VIEW_ACCESS")
MATOMO_INSTANCE = os.getenv("MATOMO_INSTANCE")


# App Settings environment variables
c_CSRF_FAILURE_VIEW = os.getenv("c_CSRF_FAILURE_VIEW")
c_CSRF_USE_SESSION = os.getenv("c_CSRF_USE_SESSION")
c_CSRF_COOKIE_SECURE = os.getenv("c_CSRF_COOKIE_SECURE")
c_CSRF_TRUSTED_ORIGINS = os.getenv("c_CSRF_TRUSTED_ORIGINS").split(",")
c_CSRF_COOKIE_SAMESITE = os.getenv("c_CSRF_COOKIE_SAMESITE")
c_ALLOWED_HOSTS = os.environ.get("c_ALLOWED_HOSTS").split(",")
c_DEBUG = os.getenv("c_DEBUG", False).lower() in ('true', '1', 't')
c_hostname = os.getenv("c_hostname")
c_POSTGRES_DB = os.getenv("POSTGRES_DB")
c_POSTGRES_USER = os.getenv("POSTGRES_USER")
c_POSTGRES_HOST = os.getenv("POSTGRES_HOST")
c_POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
c_POSTGRES_PORT = os.getenv("POSTGRES_PORT")

# Follow the steps below to generate a Django secret key:

# Access the Python Interactive Shell
# Import get_random_secret_key() from django.core.management.utils.
# Generate the Secret Key in the Terminal using the get_random_secret_key() function
# Copy and Paste the Key into your SECRET_KEY variable in the const.py
c_SECRET_KEY = os.getenv("c_SECRET_KEY")
