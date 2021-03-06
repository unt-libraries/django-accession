from djqscsv import render_to_csv_response

from django.apps import apps
from django.http import Http404
from django.db.models.fields.related import RelatedField
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from accession.admin import accession_admin
from accession.utils import get_csv_config


@staff_member_required
def print_view(request, app_label, model_name, object_id):
    """Print view for the accession object model"""
    # Get the model
    try:
        model = apps.get_model(app_label, model_name)
    except LookupError:
        raise Http404("Model not found.")

    try:
        row = model.objects.get(id__exact=int(object_id))
    except model.DoesNotExist:
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
                    # Get the row in the related model, based on the id
                    try:
                        value = related_model.objects.get(
                            id__exact=int(row.__dict__[key]),
                            )
                    except Exception:
                        pass
                    else:
                        break
        # if it isn't a related field
        else:
            # get the value of the field
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
        model = apps.get_model(app, model)
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

    # Retrieve the configuration object for the given model.
    csv_config = get_csv_config(model)

    # Use the fields list from the configuration object to filter the fields
    # that are shown in the queryset.
    results = results.values(*csv_config.fields)

    # Use the two dicts from the configuration object to define new columns in
    # the csv doc and rename the fields to be more readable.
    return render_to_csv_response(
        results,
        field_header_map=csv_config.header_map,
        field_serializer_map=csv_config.serializer_map,
        streaming=False,
    )
