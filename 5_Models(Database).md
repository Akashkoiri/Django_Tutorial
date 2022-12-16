## Models Creation & Conection with Postgres Database 

---

### 1. First create a database called arjtech using pgadmin.

### 2. In settings.py file of django project :

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arjtech',  # Database Name
        'USER': 'postgres',
        'PASSWORD': 'akash1826',
        'HOST': '127.0.0.1'
    }
}
```

### 3. Connect django with postgres.

```sh
# This is a postgres database adapter or connecter which connect with python
pip install psycopg2 
```

### 4. Convert the Class into a Model

```py
class Destinations(models.Model):
	# Don't need any id field because it will be added automaticlly inside the  database

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='uploads')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
```

### 5. Create & Make the Migrations.

```sh
python manage.py makemigrations

# You can verify migration with this command
python manage.py sqlmigrate <app_name> <migratation_no.>

# This will create a table in the database
python manage.py migrate
```

### Remigration :

```sh
# Change somthing in models.py file & then run
python manage.py makemigrations
python manage.py migrate
```