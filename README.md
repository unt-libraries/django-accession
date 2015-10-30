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

4. Sync the database.
    ```sh
        $ docker-compose run --rm web python manage.py syncdb
    ```
    When prompted, create a superuser so you can access the admin sites.
    This step only needs to be done the first time you start the container.

5. Start the container as a daemon.
    ```sh
        $ docker-compose up -d
        # Use 'docker-compose stop' to stop the container.
    ```
    At this point you should be able to access your local instance of the site by visiting `<dockerhost_ip>:8000/tfc/databrowse`.

6. If desired, run the tests.
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
