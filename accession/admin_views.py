from djqscsv import render_to_csv_response

from django.db import models
from django.http import Http404
from django.db.models.fields.related import RelatedField
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from accession.admin import accession_admin
from accession.models import Accession, Donor, Object


@staff_member_required
def print_view(request, app_label, model_name, object_id):
    """Print view for the accession object model"""
    # Get the model
    try:
        model = models.get_model(app_label, model_name)
    except LookupError:
        raise Http404("Model not found.")

    try:
        row = model.objects.get(id__exact=int(object_id))
    except:
        raise Http404("Object not found.")

    field_list = []
    # Loop through the field's and assign the values to the labels
    for field in model._meta.fields:
        value = ''
        # if the field is a related field (ForeignKey, ManyToMany, OneToOne)
        if isinstance(field, RelatedField):
            # get the related model from the field object
            related_model = field.rel.to
            for key in row.__dict__.keys():
                # find the field in the row that matches the related field
                if key.startswith(field.name):
                    # Get the unicode version of the row in the related model, based on the id
                    try:
                        entry = related_model.objects.get(
                            id__exact=int(row.__dict__[key]),
                            )
                    except:
                        pass
                    else:
                        value = entry.__unicode__().encode("utf-8")
                        break
        # if it isn't a related field
        else:
            # get the value of the field
            if isinstance(row.__dict__[field.name], basestring):
                value = row.__dict__[field.name].encode("utf-8")
            else:
                value = row.__dict__[field.name]
        field_list.append({'label': field.verbose_name, 'value': value})

    return render(
        request,
        "admin/accession/print_view.html",
        {
            'requested_obj': row,
            'app_name': app_label.title(),
            'model_name': model_name.title(),
            'field_list': field_list,
        },
    )


def export_csv(request, app, model):
    try:
        model = models.get_model(app, model)
    except (AttributeError, LookupError) as e:
        raise Http404(str(e))

    kwargs = request.GET.dict()
    q = kwargs.pop('q', '')
    objects_list = model.objects.all()
    if kwargs:
        objects_list = model.objects.filter(**kwargs)

    # Using one of Django's private API's (_registry). May break with updates.
    model_admin = accession_admin._registry[model]
    results, _ = model_admin.get_search_results(request, objects_list, q)

    # Modify the querysets to show something more meaningful than object IDs.
    field_serializer_map = {}
    field_header_map = {}

    if model == Accession:
        field_serializer_map = {'donor_id': (lambda x: str(Donor.objects.get(id=x)))}
        field_header_map = {'donor_id': 'donor'}

    elif model == Donor:
        fields_to_show = [
            'id', 'salutation', 'first_name', 'middle_name', 'last_name',
            'organization_name', 'donor_type', 'gender', 'address_1',
            'address_2', 'city__city', 'state', 'postal_code',
            'country__country', 'phone_number_1', 'phone_number_2',
            'email_address', 'comments'
        ]

        field_header_map = {'city__city': 'city', 'country__country': 'country'}

        results = results.values(*fields_to_show)

    elif model == Object:
        fields_to_show = [
            'id', 'object_number', 'accession_number__accession_number',
            'object_description', 'related_objects', 'original_numbers',
            'date_object_creation', 'object_era', 'remarks', 'location_remarks',
            'construction', 'exhibitions', 'publications', 'provenance',
            'condition_statement', 'price', 'public_notes',
            'designer__designer', 'label__label', 'retailer__retailer_name',
            'retailer_label__retailer_label', 'classification__classification',
            'country__country', 'gender', 'location__location',
            'condition__condition', 'material__material',
            'measurement__measurement', 'type__object_type', 'parts__part',
            'date_record_added', 'date_record_last_edited'
        ]

        field_header_map = {
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

        results = results.values(*fields_to_show)

    return render_to_csv_response(results, field_header_map=field_header_map,
                                  field_serializer_map=field_serializer_map)
