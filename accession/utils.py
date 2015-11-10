from django.db.models import Count

from accession import models


class ModelNotFound(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def find_duplicates(model_str):
    """Finds all table entries that have the same value in a certain field.

    This function takes a model string and returns a list of
    lists containing the count and field name for all found duplicates.
    For example, if there was a model 'Dogs' with a field 'name', and two of
    the entries shared the same name 'Ralf', then the returned results would
    be the following:
        >>>find_duplicates(Dogs, 'name')
        [[2, 'Ralf']]
    """

    model_field_map = {
        'accession': [models.Accession, 'accession_number'],
        'city': [models.City, 'city'],
        'classification': [models.Classification, 'classification'],
        'condition': [models.Condition, 'condition'],
        'country': [models.Country, 'country'],
        'designer': [models.Designer, 'designer'],
        'donor': [models.Donor, 'last_name'],
        'label': [models.Label, 'label'],
        'location': [models.Location, 'location'],
        'material': [models.Material, 'material'],
        'measurement': [models.Measurement, 'measurement'],
        'object': [models.Object, 'object_number'],
        'part': [models.Part, 'part'],
        'retailer_label': [models.Retailer_Label, 'retailer_label'],
        'retailer': [models.Retailer, 'retailer'],
        'type': [models.Type, 'object_type']
    }

    # Map the model string to the model class and field.
    try:
        model, field = model_field_map[model_str]
    except KeyError:
        raise ModelNotFound('{} is not a known model.'.format(model_str))

    # This query gets a count of duplicates and the value of the field.
    queryset = (model.objects.values(field)
                             .annotate(count=Count('pk'))
                             .filter(count__gt=1)
                             .order_by('-count'))

    # Convert list of dicts into a list of lists, as expected by the template.
    results = []
    for result in queryset:
        results.append([result['count'], result[field]])

    return results
