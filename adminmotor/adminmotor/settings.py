"""
Django settings for adminmotor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't=o@wl&#*+g^jrp_q^$#abk0z00kyo9^f@93-y#!_1(djl9*3&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'app',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ( 
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.csrf",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
   
)

ROOT_URLCONF = 'adminmotor.urls'

WSGI_APPLICATION = 'adminmotor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adminmotor',
        'USER': 'root',
        'PASSWORD': 'mayra',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    #'social.backends.amazon.AmazonOAuth2',
    #'social.backends.angel.AngelOAuth2',
    #'social.backends.aol.AOLOpenId',
    #'social.backends.appsfuel.AppsfuelOAuth2',
    #'social.backends.behance.BehanceOAuth2',
    #'social.backends.belgiumeid.BelgiumEIDOpenId',
    #'social.backends.bitbucket.BitbucketOAuth',
    #'social.backends.box.BoxOAuth2',
    #'social.backends.coinbase.CoinbaseOAuth2',
    #'social.backends.dailymotion.DailymotionOAuth2',
    #'social.backends.disqus.DisqusOAuth2',
    #'social.backends.douban.DoubanOAuth2',
    #'social.backends.dropbox.DropboxOAuth',
    #'social.backends.evernote.EvernoteSandboxOAuth',
    #'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    #'social.backends.fedora.FedoraOpenId',
    #'social.backends.fitbit.FitbitOAuth',
    #'social.backends.flickr.FlickrOAuth',
    #'social.backends.foursquare.FoursquareOAuth2',
    #'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GooglePlusAuth',
    #'social.backends.instagram.InstagramOAuth2',
    #'social.backends.jawbone.JawboneOAuth2',
    #'social.backends.linkedin.LinkedinOAuth',
    #'social.backends.linkedin.LinkedinOAuth2',
    #'social.backends.live.LiveOAuth2',
    #'social.backends.livejournal.LiveJournalOpenId',
    #'social.backends.mailru.MailruOAuth2',
    #'social.backends.mendeley.MendeleyOAuth',
    #'social.backends.mixcloud.MixcloudOAuth2',
    #'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    #'social.backends.open_id.OpenIdAuth',
    #'social.backends.openstreetmap.OpenStreetMapOAuth',
    #'social.backends.orkut.OrkutOAuth',
    #'social.backends.persona.PersonaAuth',
    #'social.backends.podio.PodioOAuth2',
    #'social.backends.rdio.RdioOAuth1',
    #'social.backends.rdio.RdioOAuth2',
    #'social.backends.readability.ReadabilityOAuth',
    #'social.backends.reddit.RedditOAuth2',
    #'social.backends.runkeeper.RunKeeperOAuth2',
    #'social.backends.skyrock.SkyrockOAuth',
    #'social.backends.soundcloud.SoundcloudOAuth2',
    #'social.backends.stackoverflow.StackoverflowOAuth2',
    #'social.backends.steam.SteamOpenId',
    #'social.backends.stocktwits.StocktwitsOAuth2',
    #'social.backends.stripe.StripeOAuth2',
    #'social.backends.suse.OpenSUSEOpenId',
    #'social.backends.thisismyjam.ThisIsMyJamOAuth1',
    #'social.backends.trello.TrelloOAuth',
    #'social.backends.tripit.TripItOAuth',
    #'social.backends.tumblr.TumblrOAuth',
    #'social.backends.twilio.TwilioAuth',
    'social.backends.twitter.TwitterOAuth',    
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'
URL_PATH = ''
