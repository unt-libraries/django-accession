Change Log
==========


x.x.x
-----

* Fixed flake8 indentation error.


2.0.0
-----

* Reworked tox.ini and .travis.yml to allow for easier test environment expansion later on.
* Made except clauses catch specific exceptions.
* Made some changes to test setup to comply with newer versions of Django.
* Updated dependencies and app to now work with Django 1.8 - 1.11.
* Updated some Django import paths.
* Named the print URL.
* Changed how the history and print URLs were formed so they work with all of our supported versions of Django.
* Dropped support for Django 1.7.


1.1.2
-----

* Added `organization_name` to the `DonorAdmin` `search_fields` to fix retrieval on Donor names. [#17](https://github.com/unt-libraries/django-accession/issues/17)


1.1.1
-----

* Changed the way that some of the fields' titles are assigned in the CSV export
feature to make them more easily understood.


1.1.0
-----

* Added "Export to CSV" link to admin pages.
* Removed duplicates view.
* Changed csv export behavior to work with searches and filters (exporting just the results shown).
* Made the "Export to CSV" and the "Print" link work from the test project's admin
site (used to only work from the app's admin site)


1.0.0
-----

Initial Release
