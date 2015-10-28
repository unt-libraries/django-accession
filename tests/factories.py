from datetime import datetime

import factory
from factory import fuzzy

from accession import models


class DesignerFactory(factory.django.DjangoModelFactory):
    designer = fuzzy.FuzzyText(length=100)

    class Meta:
        model = models.Designer


class LabelFactory(factory.django.DjangoModelFactory):
    label = fuzzy.FuzzyText(length=200)

    class Meta:
        model = models.Label


class ClassificationFactory(factory.django.DjangoModelFactory):
    classification = fuzzy.FuzzyText(length=50)

    class Meta:
        model = models.Classification


class LocationFactory(factory.django.DjangoModelFactory):
    location = fuzzy.FuzzyText(length=50)

    class Meta:
        model = models.Location


class ConditionFactory(factory.django.DjangoModelFactory):
    condition = fuzzy.FuzzyText(length=50)

    class Meta:
        model = models.Condition


class DonorFactory(factory.django.DjangoModelFactory):
    first_name = fuzzy.FuzzyText(length=20)
    last_name = fuzzy.FuzzyText(length=20)
    organization_name = fuzzy.FuzzyText(length=20)
    donor_type = fuzzy.FuzzyChoice(['PER', 'ORG'])

    class Meta:
        model = models.Donor


class AccessionFactory(factory.django.DjangoModelFactory):
    accession_number = factory.Sequence(lambda n: str(n))
    donor = factory.SubFactory(DonorFactory)
    anonymous_accession = False
    date_paperwork_sent = fuzzy.FuzzyNaiveDateTime(datetime(2012, 1, 1))
    date_paperwork_returned = fuzzy.FuzzyNaiveDateTime(datetime(2012, 1, 2))

    class Meta:
        model = models.Accession


class ObjectFactory(factory.django.DjangoModelFactory):
    object_number = factory.Sequence(lambda n: str(n))
    accession_number = factory.SubFactory(AccessionFactory)
    object_description = fuzzy.FuzzyText()
    classification = factory.SubFactory(ClassificationFactory)
    designer = factory.SubFactory(DesignerFactory)
    label = factory.SubFactory(LabelFactory)
    gender = 'M'
    location = factory.SubFactory(LocationFactory)
    condition = factory.SubFactory(ConditionFactory)

    class Meta:
        model = models.Object
