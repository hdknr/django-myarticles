SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'bootstrap3',
    'ordered_model',
    'myarticles',
    'tests',
    'django_nose',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqllite3',
        'TEST_NAME': 'test.sqllite3',
        # 'NAME': ':memory:',
    }
}
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
