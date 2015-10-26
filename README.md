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
        $ pip install git+git://github.com/unt-libraries/django-accession.git
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

4. Sync the database.
    ```sh
        $ python manage.py syncdb
    ```


Developing
----------

1. [Install Docker](http://docs.docker.com/installation/).

2. Install Docker Compose.
    ```sh
        $ pip install docker-compose
    ```

3. Clone the repository.
    ```sh
        $ git clone https://github.com/unt-libraries/django-accession
    ```

4. Warm-up the database. It will take 10-15 seconds to complete after it has been pulled from the Docker Hub.
    ```sh
        $ docker-compose up -d db
    ```

5. Sync the database.
    ```sh
        $ docker-compose run --rm web python manage.py syncdb
    ```

6. Start the containers as daemons.
    ```sh
        $ docker-compose up -d
        # Use 'docker-compose stop' to stop the containers.
    ```
    At this point you should be able to access your local instance of the site by visiting <dockerhost>:8000/tfc/databrowse.

7. If desired, run the tests.
    ```sh
        $ docker-compose run --rm web tox
    ```

License
-------

See LICENSE.txt.


Contributors
------------

* Brandon Fredericks
* [Mark Phillips](https://github.com/vphill)
* [Joey Liechty](https://github.com/yeahdef)
* [Gio Gottardi](https://github.com/somexpert)
