from django.db import models
from localflavor.us.us_states import STATE_CHOICES

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

SALUTATION_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MISS', 'Miss'),
    ('MS', 'Ms.'),
    ('MRMRS', 'Mr. and Mrs.'),
    ('DR', 'Dr.'),
)

DONOR_TYPE_CHOICES = (
    ('PER', 'Person'),
    ('ORG', 'Organization'),
    )

ACQUISITION_METHOD_CHOICES = (
    ('GIK', 'Gift In Kind'),
    ('TRN', 'Transfer'),
    ('PUR', 'Purchase'),
    ('OTH', 'Other'),
    )

YOUR_STATE_CHOICES = list(STATE_CHOICES)

ERA_CHOICES = (
    ('Pre-1770', 'Pre-1770'),
    ('1770-1779', '1770-1779'),
    ('1780-1789', '1780-1789'),
    ('1790-1799', '1790-1799'),
    ('1800-1809', '1800-1809'),
    ('1810-1819', '1810-1819'),
    ('1820-1829', '1820-1829'),
    ('1830-1839', '1830-1839'),
    ('1840-1849', '1840-1849'),
    ('1850-1859', '1850-1859'),
    ('1860-1869', '1860-1869'),
    ('1870-1879', '1870-1879'),
    ('1880-1889', '1880-1889'),
    ('1890-1899', '1890-1899'),
    ('1900-1909', '1900-1909'),
    ('1910-1919', '1910-1919'),
    ('1920-1929', '1920-1929'),
    ('1930-1939', '1930-1939'),
    ('1940-1949', '1940-1949'),
    ('1950-1959', '1950-1959'),
    ('1960-1969', '1960-1969'),
    ('1970-1979', '1970-1979'),
    ('1980-1989', '1980-1989'),
    ('1990-1999', '1990-1999'),
    ('2000-2009', '2000-2009'),
    ('2010-2019', '2010-2019'),
)

OBJECT_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unisex'),
    ('UnKn', 'Gender Unknown'),
    ('UnRec', 'Not Recorded'),
    ('NA', 'Not Applicable'),
)


class Accession(models.Model):
    accession_number = models.CharField(max_length=12, unique=True)
    donor = models.ForeignKey("Donor")
    date_received = models.DateField(blank=True, null=True)
    description = models.TextField(
        help_text="Publicly viewable description of the accession")
    date_in_computer = models.DateField(blank=True, null=True)
    acquisition_method = models.CharField(
        max_length=3, choices=ACQUISITION_METHOD_CHOICES, default="GIK")
    anonymous_accession = models.BooleanField(
        help_text="Check if accession should be listed as anonymous on any public interface")
    date_paperwork_sent = models.DateField(
        blank=True,
        null=True,
        help_text="Date recipt of gift (ROG) was mailed out")
    date_paperwork_returned = models.DateField(
        blank=True,
        null=True,
        help_text="Date signed recipt of gift (ROG) was received")
    accession_note = models.TextField(
        blank=True,
        help_text="Private note related to this accession")

    def __unicode__(self):
        return self.accession_number

    class Meta:
        ordering = ["accession_number"]

    def has_date_paperwork_sent(self):
        return self.date_paperwork_sent is not None
    has_date_paperwork_sent.short_description = "Paperwork Sent"
    has_date_paperwork_sent.boolean = True

    def has_date_paperwork_returned(self):
        return self.date_paperwork_returned is not None
    has_date_paperwork_returned.short_description = "Paperwork Returned"
    has_date_paperwork_returned.boolean = True


class Donor(models.Model):
    salutation = models.CharField(max_length=5, blank=True, choices=SALUTATION_CHOICES)
    first_name = models.CharField(blank=True, max_length=100)
    middle_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    organization_name = models.CharField(blank=True, max_length=255)
    donor_type = models.CharField(
        max_length=3,
        blank=True,
        choices=DONOR_TYPE_CHOICES,
        default="PER")
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.ForeignKey("City", blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, choices=YOUR_STATE_CHOICES)
    postal_code = models.CharField(max_length=15, blank=True)
    country = models.ForeignKey("Country", blank=True, null=True)
    phone_number_1 = models.CharField(
        max_length=25,
        blank=True,
        help_text="Please use the following format: <em>(940) 391-0414</em>.")
    phone_number_2 = models.CharField(
        max_length=25,
        blank=True,
        help_text="Please use the following format: <em>(940) 391-0414</em>.")
    email_address = models.EmailField(blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    @property
    def full_name(self):
        if self.donor_type == "ORG":
            return u'%s' % self.organization_name
        else:
            return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s' % self.full_name


class City(models.Model):
    city = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["city"]
        verbose_name_plural = "Cities"

    def __unicode__(self):
        return self.city


class Country(models.Model):
    # CHANGE-BACK once database cleanup is done to make unique=True
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ["country"]
        verbose_name_plural = "Countries"

    def __unicode__(self):
        return self.country


class Designer(models.Model):
    # CHANGE-BACK once database cleanup is done to make unique=True
    designer = models.CharField(max_length=200)

    class Meta:
        ordering = ["designer"]

    def __unicode__(self):
        return self.designer


class Label(models.Model):
    # CHANGE-BACK once database cleanup is done to make unique=True
    label = models.CharField(max_length=200, verbose_name="Designer Label")

    class Meta:
        ordering = ["label"]

    def __unicode__(self):
        return self.label


class Retailer(models.Model):
    retailer_name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["retailer_name"]

    def __unicode__(self):
        return self.retailer_name


class Retailer_Label(models.Model):
    retailer_label = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Retailer Label",
        )

    class Meta:
        ordering = ["retailer_label"]
        verbose_name_plural = "Retailer Labels"

    def __unicode__(self):
        return self.retailer_label


class Classification(models.Model):
    classification = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["classification"]

    def __unicode__(self):
        return self.classification


class Location(models.Model):
    # CHANGE-BACK once database cleanup is done to make unique=True
    location = models.CharField(max_length=200)

    class Meta:
        ordering = ["location"]

    def __unicode__(self):
        return self.location


class Condition(models.Model):
    condition = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["condition"]

    def __unicode__(self):
        return self.condition


class Material(models.Model):
    # CHANGE-BACK once database cleanup is done to make unique=True
    material = models.CharField(max_length=200)

    class Meta:
        ordering = ["material"]

    def __unicode__(self):
        return self.material


class Measurement(models.Model):
    # CHANGE-BACK once database cleanup is done to make unique=True
    measurement = models.CharField(max_length=200)

    class Meta:
        ordering = ["measurement"]

    def __unicode__(self):
        return self.measurement


class Type(models.Model):
    object_type = models.CharField(max_length=200)

    class Meta:
        ordering = ["object_type"]

    def __unicode__(self):
        return self.object_type


class Part(models.Model):
    part = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["part"]

    def __unicode__(self):
        return self.part


class Object(models.Model):
    # object_number needs to be changed to unique=True after editing.
    object_number = models.CharField(max_length=20)
    accession_number = models.ForeignKey("Accession")
    object_description = models.TextField()
    related_objects = models.CharField(max_length=200, blank=True)
    original_numbers = models.CharField(max_length=100, blank=True)
    date_object_creation = models.CharField(max_length=100, blank=True)
    object_era = models.CharField(max_length=10, choices=ERA_CHOICES, blank=True)
    remarks = models.TextField(blank=True)
    location_remarks = models.TextField(blank=True)
    construction = models.TextField(blank=True)
    exhibitions = models.TextField(blank=True)
    publications = models.TextField(blank=True)
    provenance = models.TextField(blank=True)
    condition_statement = models.TextField(blank=True)
    price = models.DecimalField(blank=True, max_digits=8, decimal_places=2, null=True)
    public_notes = models.TextField(blank=True)
    designer = models.ForeignKey("Designer", blank=True, null=True)
    label = models.ForeignKey("Label", blank=True, null=True, verbose_name='Designer Label')
    retailer = models.ForeignKey("Retailer", blank=True, null=True)
    retailer_label = models.ForeignKey(
        "Retailer_Label",
        blank=True,
        null=True,
        verbose_name="Retailer Label")
    classification = models.ForeignKey("Classification")
    country = models.ForeignKey("Country", blank=True, null=True)
    gender = models.CharField(max_length=14, choices=OBJECT_GENDER_CHOICES)
    location = models.ForeignKey("Location")
    condition = models.ForeignKey("Condition")
    material = models.ForeignKey("Material", blank=True, null=True)
    measurement = models.ForeignKey("Measurement", blank=True, null=True)
    type = models.ForeignKey("Type", blank=True, null=True)
    parts = models.ForeignKey("Part", blank=True, null=True)

    date_record_added = models.DateTimeField(auto_now_add=True)
    date_record_last_edited = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.object_number

    def showLabel(self):
        return self.label
    showLabel.short_description = "Label"

    def showLocation(self):
        return self.location
    showLocation.short_description = "Location"

    def showDesigner(self):
        if self.designer:
            return self.designer.designer
    showDesigner.short_description = "Designer"
