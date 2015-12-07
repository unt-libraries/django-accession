from djqscsv import render_to_csv_response

from django.db import models
from django.http import Http404
from django.db.models.fields.related import RelatedField
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from accession.admin import accession_admin


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

    q = ''
    if request.GET:
        kwargs = request.GET.dict()
        q = kwargs.pop('q', '')
        model_fields_fullname = model._meta.fields
        model_fields = [str(f).split('.')[-1] for f in model_fields_fullname]
        valid_request_fields = set(model_fields) & set(kwargs)
        kwargs = {k: kwargs[k] for k in valid_request_fields}

        objects_list = model.objects.filter(**kwargs)

    else:
        objects_list = model.objects.all()

    model_admin = accession_admin._registry[model]
    queried_objects_list = model_admin.get_search_results(request, objects_list, q)[0]
    return render_to_csv_response(queried_objects_list)
