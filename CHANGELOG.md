Change Log
==========

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
