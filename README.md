Django Accession
================

[![Build Status](https://travis-ci.org/unt-libraries/django-accession.svg?branch=master)](https://travis-ci.org/unt-libraries/django-accession)


About
-----

This app is used to store information about the items in the Texas Fashion
Collection: a repository operated by the University of North Texas. Users are
provided with a Django admin interface to enter and view information such as
color, style, location, etc. The data may also be exported in csv
(comma-separated-values) format.


Requirements
------------

* Python 2.7
* Django 1.7 or 1.8


Installation
------------

1. Install from GitHub.
    ```sh
        $ pip install git+git://github.com/unt-libraries/django-accession.git
    ```

2. Add app and dependency to INSTALLED_APPS.
    ```python
        INSTALLED_APPS = (
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

4. Apply migrations.
    ```sh
        $ python manage.py migrate
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

4. Start the container as a daemon.
    ```sh
        $ docker-compose up -d
        # Use 'docker-compose stop' to stop the container.
    ```
    At this point you should be able to access your local instance of the site by visiting `<dockerhost_ip>:8000/tfc/admin`.

5. Create a superuser for access to the admin sites.
    ```sh
        $ docker-compose run --rm web python manage.py createsuperuser
    ```

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
