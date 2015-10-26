Django Accession
================


About
-----


Requirements
------------

* Django 1.6


Installation
------------

1. Install from GitHub.
    ```sh
        $ pip install git+git://github.com/unt-libraries/django-controlled-vocabularies.git
    ```

2. Add app and dependency to INSTALLED_APPS.
    ```python
        INSTALLED_APPS = (
            'django_databrowse',
            'accession',
        )
    ```

3. Include the URLs.
    ```python
        urlpatterns = [
            url(r'^admin/', include(admin.site.urls)),
            url(r'^tfc/', include('accession.urls')),
        ]
    ```

4. Sync the database and create a superuser account.
    ```sh
        $ python manage.py syncdb
    ```


Developing
----------

1. [Install Docker](http://docs.docker.com/installation/)

2. Install Docker Compose
    ```sh
        $ pip install docker-compose
    ```

3. Clone the repository.
    ```sh
        $ git clone https://github.com/unt-libraries/django-controlled-vocabularies
    ```

4. Build the images.
    ```sh
        $ docker-compose build
    ```

5. Allow the database to initialize everything (only needed the first time the image is loaded).
    ```sh
        $ docker-compose up db
    ```
    Wait until the output stops, then execute the following to stop the container.
    ```sh
        $ docker-compose stop db
    ```

6. Start the containers as daemons.
    ```sh
        $ docker-compose up -d
    ```

7. Sync the database and create a superuser account.
    ```sh
        $ docker-compose run --rm web python manage.py syncdb
    ```
    At this point you should be able to access your local instance of the site by visiting <dockerhost>:8000/tfc/databrowse

9. If desired, run the tests.
    ```sh
        $ docker-compose run --rm web tox
    ```

License
-------

See LICENSE.txt


Contributors
------------

* Brandon Fredericks
* [Mark Phillips](https://github.com/vphill)
* [Joey Liechty](https://github.com/yeahdef)
* [Gio Gottardi](https://github.com/somexpert)
