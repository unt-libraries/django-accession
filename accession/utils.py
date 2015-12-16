"""This module is for code which assists the views."""

from accession.models import Accession, Donor, Object


def get_csv_config(model):
    """Returns configurations for exporting querysets to csv based on the model.

    This function takes a model and returns a list and two dictionaries. The
    list (fields) dictates which fields are to be returned in a queryset from
    the given model. The first dictionary (serializer_map) maps new fields to
    their data, and is used here to return the string representation of a
    foreign key in the Accession model. The second dictionary (header_map)
    renames field names. It is used to make the final csv output more easily
    readable. The list and dictionaries are determined by what model is given.
    """
    if model == Accession:
        return AccessionCSVConfig

    elif model == Donor:
        return DonorCSVConfig

    elif model == Object:
        return ObjectCSVConfig

    else:
        return GenericCSVConfig


class AccessionCSVConfig(object):
    fields = []
    serializer_map = {
        'donor_id': (lambda x: str(Donor.objects.get(id=x)))
    }
    header_map = {
        'donor_id': 'donor'
    }


class DonorCSVConfig(object):
    fields = [
        'id',
        'salutation',
        'first_name',
        'middle_name',
        'last_name',
        'organization_name',
        'donor_type',
        'gender',
        'address_1',
        'address_2',
        'city__city',
        'state',
        'postal_code',
        'country__country',
        'phone_number_1',
        'phone_number_2',
        'email_address',
        'comments'
    ]
    serializer_map = {}
    header_map = {
        'city__city': 'city',
        'country__country': 'country'
    }


class ObjectCSVConfig(object):
    fields = [
        'id',
        'object_number',
        'accession_number__accession_number',
        'object_description',
        'related_objects',
        'original_numbers',
        'date_object_creation',
        'object_era',
        'remarks',
        'location_remarks',
        'construction',
        'exhibitions',
        'publications',
        'provenance',
        'condition_statement',
        'price',
        'public_notes',
        'designer__designer',
        'label__label',
        'retailer__retailer_name',
        'retailer_label__retailer_label',
        'classification__classification',
        'country__country',
        'gender',
        'location__location',
        'condition__condition',
        'material__material',
        'measurement__measurement',
        'type__object_type',
        'parts__part',
        'date_record_added',
        'date_record_last_edited'
    ]
    serializer_map = {}
    header_map = {
        'accession_number__accession_number': 'accession number',
        'designer__designer': 'designer',
        'label__label': 'label',
        'retailer__retailer_name': 'retailer',
        'retailer_label__retailer_label': 'retailer label',
        'classification__classification': 'classification',
        'country__country': 'country',
        'location__location': 'location',
        'condition__condition': 'condition',
        'material__material': 'material',
        'measurement__measurement': 'measurement',
        'type__object_type': 'type',
        'parts__part': 'parts'
    }


class GenericCSVConfig(object):
    fields = []
    serializer_map = {}
    header_map = {}
