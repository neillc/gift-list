import os
from app import app


def key_missing(key):
    app.logger.warning('{key} is not set'.format(key=key))


class Config(object):
    # Absoultely essential settings - the app cannot do anything without these
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECURITY_CONFIRMABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True

    if 'ADMIN_EMAIL' in os.environ:
        ADMIN_EMAIL = os.environ['ADMIN_EMAIL']
    else:
        ADMIN_EMAIL = 'admin@localhost'

    if 'ADMIN_PASSWD' in os.environ:
        ADMIN_PASSWD = os.environ['ADMIN_PASSWD']
    else:
        ADMIN_PASSWD = 'secrete'

    # Important settings that some functions may work without (e.g. migrations)
    if 'SECRET_KEY' in os.environ:
        SECRET_KEY = os.environ['SECRET_KEY']
    else:
        key_missing('SECRET_KEY')

    if 'MAIL_SERVER' in os.environ:
        MAIL_SERVER = os.environ['MAIL_SERVER']
    else:
        key_missing('MAIL_SERVER')

    if 'MAIL_PORT' in os.environ:
        MAIL_PORT = os.environ['MAIL_PORT']
    else:
        key_missing('MAIL_PORT')

    if 'MAIL_USE_SSL' in os.environ:
        MAIL_USE_SSL = os.environ['MAIL_USE_SSL']
    else:
        key_missing('MAIL_USE_SSL')

    if 'MAIL_USERNAME' in os.environ:
        MAIL_USERNAME = os.environ['MAIL_USERNAME']
    else:
        key_missing('MAIL_USERNAME')

    if 'MAIL_PASSWORD' in os.environ:
        MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    else:
        key_missing('MAIL_PASSWORD')

    if 'SECURITY_EMAIL_SENDER' in os.environ:
        SECURITY_EMAIL_SENDER = os.environ['SECURITY_EMAIL_SENDER']
    else:
        key_missing('SECURITY_EMAIL_SENDER')

    # SECURITY_EMAIL_SENDER = 'neill@ingenious.com.au' # TOBLOG need this for confirm email to work

    # Optional config parameters - no harm if these are not present
    CONFIG_SOCIAL = False

    if 'TWITTER_KEY' in os.environ:
        SOCIAL_TWITTER = {
            'consumer_key': os.environ['TWITTER_KEY'],
            'consumer_secret': os.environ['TWITTER_SECRET']
        }
        CONFIG_SOCIAL = True
    else:
        SOCIAL_TWITTER = None

    if 'FB_ID' in os.environ:
        SOCIAL_FACEBOOK = {
            'consumer_key': os.environ['FB_ID'],
            'consumer_secret': os.environ['FB_SECRET']
        }
        CONFIG_SOCIAL = True
    else:
        SOCIAL_FACEBOOK = None

    if 'GOOGLE_ID' in os.environ:
        SOCIAL_GOOGLE = {
            'consumer_key': os.environ['GOOGLE_ID'],
            'consumer_secret': os.environ['GOOGLE_SECRET']
        }
        CONFIG_SOCIAL = True
    else:
        SOCIAL_GOOGLE = None


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
