# gift-list
A gift list application to help us with Christmas shopping next year

This application is designed to be configured via environment variables.

The following configuration variables are supported:

* DEBUG (defaults to False if not specified)
* TESTING (defaults to False if not specified)
* CSRF_ENABLED (defaults to False if not specified)
* SQLALCHEMY_DATABASE_URI (required)
* SECURITY_CONFIRMABLE (defaults to True if not specified)
* SECURITY_TRACKABLE (defaults to True if not specified)
* SECURITY_REGISTERABLE (defaults to True if not specified)
* ADMIN_EMAIL (defaults to 'admin@localhost' if not specified)
* ADMIN_PASSWD (defaults to 'secrete' if not specified) Don't leave this as default!
* SECRET_KEY (some scripts will work without this, but the server won't run).
* MAIL_SERVER (some scripts will work without this, but the server won't run).
* MAIL_PORT (some scripts will work without this, but the server won't run).
* MAIL_USE_SSL (some scripts will work without this, but the server won't run).
* MAIL_USERNAME (some scripts will work without this, but the server won't run).
* MAIL_PASSWORD (some scripts will work without this, but the server won't run).
* SECURITY_EMAIL_SENDER  (some scripts will work without this, but the server won't run).
* TWITTER_KEY (optional)
* TWITTER_SECRET (optional)
* FB_ID (optional)
* FB_SECRET (optional)
* GOOGLE_ID (optional)
* GOOGLE_SECRET (optional)