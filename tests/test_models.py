import pytest

from accession import models

from .factories import DonorFactory, AccessionFactory, ObjectFactory

pytestmark = pytest.mark.django_db


class TestAccession:
    def test_has_date_paperwork_sent_returns_true(self):
        accession = AccessionFactory()
        assert accession.has_date_paperwork_sent() == True

    def test_has_date_paperwork_sent_returns_false(self):
        accession = AccessionFactory(date_paperwork_sent=None)
        assert accession.has_date_paperwork_sent() == False

    def test_has_date_paperwork_returned_returns_true(self):
        accession = AccessionFactory()
        assert accession.has_date_paperwork_returned() == True

    def test_has_date_paperwork_returned_returns_false(self):
        accession = AccessionFactory(date_paperwork_returned=None)
        assert accession.has_date_paperwork_returned() == False

    def test_unicode(self):
        accession = AccessionFactory()
        assert str(accession) == accession.accession_number


class TestDonor:
    def test_full_name_donor_type_org(self):
        donor = DonorFactory(donor_type='ORG')
        assert donor.full_name == donor.organization_name

    def test_full_name_donor_type_per(self):
        donor = DonorFactory(donor_type='PER')
        assert donor.full_name == '{} {}'.format(donor.first_name, donor.last_name)

    def test_unicode(self):
        donor = DonorFactory()
        assert str(donor) == donor.full_name


class TestCity:
    def test_unicode(self):
        city = models.City.objects.create(city='Denton')
        assert str(city) == city.city


class TestCountry:
    def test_unicode(self):
        country = models.Country.objects.create(country='United States')
        assert str(country) == country.country


class TestDesigner:
    def test_unicode(self):
        designer = models.Designer.objects.create(designer='Shringle')
        assert str(designer) == designer.designer


class TestLabel:
    def test_unicode(self):
        label = models.Label.objects.create(label='Chog')
        assert str(label) == label.label


class TestRetailer:
    def test_unicode(self):
        retailer = models.Retailer.objects.create(retailer_name='Harrys')
        assert str(retailer) == retailer.retailer_name


class TestRetailerLabel:
    def test_unicode(self):
        retailer_label = models.Retailer_Label.objects.create(retailer_label='Rimps')
        assert str(retailer_label) == retailer_label.retailer_label


class TestClassification:
    def test_unicode(self):
        classification = models.Classification.objects.create(classification='Style')
        assert str(classification) == classification.classification


class TestLocation:
    def test_unicode(self):
        location = models.Location.objects.create(location='B152')
        assert str(location) == location.location


class TestCondition:
    def test_unicode(self):
        condition = models.Condition.objects.create(condition='Good')
        assert str(condition) == condition.condition


class TestMaterial:
    def test_unicode(self):
        material = models.Material.objects.create(material='Leather')
        assert str(material) == material.material


class TestMeasurement:
    def test_unicode(self):
        measurement = models.Measurement.objects.create(measurement='16')
        assert str(measurement) == measurement.measurement


class TestType:
    def test_unicode(self):
        object_type = models.Type.objects.create(object_type='Shoes')
        assert str(object_type) == object_type.object_type


class TestPart:
    def test_unicode(self):
        part = models.Part.objects.create(part='Left shoe')
        assert str(part) == part.part


class TestObject:
    def test_show_label(self):
        object_instance = ObjectFactory()
        assert object_instance.showLabel() == object_instance.label

    @pytest.mark.xfail(reason="Method doesn't take into account attribute might not exist.")
    def test_show_label_no_label(self):
        object_instance = ObjectFactory(lable=None)
        assert object_instance.showLabel() == None

    def test_show_location(self):
        object_instance = ObjectFactory()
        assert object_instance.showLocation() == object_instance.location

    def test_show_designer(self):
        object_instance = ObjectFactory()
        assert object_instance.showDesigner() == object_instance.designer.designer

    def test_show_designer_no_designer(self):
        object_instance = ObjectFactory(designer=None)
        assert object_instance.showDesigner() == None

    def test_unicode(self):
        object_instance = ObjectFactory()
        assert str(object_instance) == object_instance.object_number
