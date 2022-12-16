1. Create a file callled 'Procfile' in the project directory.
==> web: gunicorn <project_name>.wsgi --log-file -

2. In terminal on the project directory execute the command.
==> $ pip freeze > requirements.txt

3. Create a new file called 'runtime.txt' with the current python version.
==> python-3.10.7	-----(Take care of the format: Small 'p', No space)

4. In 'settings.py' file static file area should like this.
==> STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

==> $ python manage.py collectstatic

5. Push to Github