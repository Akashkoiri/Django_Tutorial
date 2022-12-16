## Django New project setup

---

[1] Create a directory with the project name (Test) 

[2] Open that in vs code

[3] $$ django-admin startproject Test .


## VS Code - Environment Setup

[5] $$ python -m venv env

[6] $$ . env/Scripts/activate

[7] (env) $$ pip install django gunicorn whitenoise

[8] $$ mkdir apps static templates


## VS Code - settings.py

```py
import os, sys

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

[9] ALLOWED_HOSTS = ['*']


[10] UTILITY_APPS = [
		'whitenoise.runserver_nostatic',
	]

	LOCAL_APPS = [
	    'travello'
	]

	INSTALLED_APPS = DEFAULT_APPS + UTILITY_APPS + LOCAL_APPS

[11] MIDDLEWARE = [
		# Add this After security (2nd)
		'whitenoise.middleware.WhiteNoiseMiddleware',	
	]

[12] INTERNAL_IPS = [	# Create this & add after middleware
    
	    "127.0.0.1",
	]

[13] TEMPLATES = [
		{
			'DIRS': [BASE_DIR, 'templates'],
		}
	]


[14] STATIC_URL = 'static/'

	 STATICFILES_DIRS = [
	 	os.path.join(BASE_DIR, 'static')
	 ]


#This is only for testing purpose do this before deployment
[16] STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')		
```