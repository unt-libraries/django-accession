from django.contrib import admin

from accession import models


class AccessionAdmin(admin.ModelAdmin):
    list_display = ['accession_number', 'donor', 'date_received',
                    'has_date_paperwork_sent', 'has_date_paperwork_returned',
                    'description', 'accession_note']
    search_fields = ['accession_number', 'description', 'accession_note',
                     'donor__first_name', 'donor__last_name',
                     'donor__organization_name']
    date_hierarchy = 'date_received'


class DonorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number_1', 'comments']
    search_fields = ['organization_name', 'first_name', 'last_name',
                     'email_address', 'comments']

    fieldsets = [
        ('Contact Info', {
            'fields': ('salutation', 'first_name', 'middle_name', 'last_name',
                       'organization_name', 'donor_type', 'gender')
        }),
        ('Address', {
            'fields': ('address_1', 'address_2', 'city', 'state',
                       'postal_code', 'country')
        }),
        ('Contact Info', {
            'fields': ('phone_number_1', 'phone_number_2', 'email_address')
        }),
        ('Comments', {
            'fields': ('comments',)
        })
    ]


class ObjectAdmin(admin.ModelAdmin):
    list_display = ['object_number', 'object_description', 'showLabel',
                    'showLocation', 'showDesigner']
    search_fields = ['object_number', 'object_description', 'remarks',
                     'public_notes', 'label__label']
    fieldsets = [(None, {
        'fields': ('object_number', 'accession_number', 'object_description',
                   'related_objects', 'original_numbers',
                   'date_object_creation', 'object_era', 'remarks',
                   'location_remarks', 'construction', 'exhibitions',
                   'publications', 'provenance', 'condition_statement',
                   'price', 'public_notes', 'designer', 'label', 'retailer',
                   'retailer_label', 'classification', 'country', 'gender',
                   'location', 'condition', 'material', 'measurement', 'type',
                   'parts'),
        'classes': ('wide',)})]


class CityAdmin(admin.ModelAdmin):
    search_fields = ['city']


class CountryAdmin(admin.ModelAdmin):
    search_fields = ['country']


class DesignerAdmin(admin.ModelAdmin):
    search_fields = ['designer']


class LabelAdmin(admin.ModelAdmin):
    search_fields = ['label']


class RetailerAdmin(admin.ModelAdmin):
    search_fields = ['retailer_name']


class Retailer_LabelAdmin(admin.ModelAdmin):
    search_fields = ['retailer_label']


class ClassificationAdmin(admin.ModelAdmin):
    search_fields = ['classification']
    fieldsets = [(None, {'fields': ('classification',), 'classes': ('wide',)})]


class LocationAdmin(admin.ModelAdmin):
    search_fields = ['location']


class ConditionAdmin(admin.ModelAdmin):
    search_fields = ['condition']


class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['material']


class MeasurementAdmin(admin.ModelAdmin):
    search_fields = ['measurement']
    fieldsets = [(None, {'fields': ('measurement',), 'classes': ('wide',)})]


class TypeAdmin(admin.ModelAdmin):
    search_fields = ['object_type']


class PartAdmin(admin.ModelAdmin):
    search_fields = ['part']


# Register all the models on both admin sites.
admin.site.register(models.Accession, AccessionAdmin)
admin.site.register(models.Donor, DonorAdmin)
admin.site.register(models.Object, ObjectAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.Designer, DesignerAdmin)
admin.site.register(models.Label, LabelAdmin)
admin.site.register(models.Retailer, RetailerAdmin)
admin.site.register(models.Retailer_Label, Retailer_LabelAdmin)
admin.site.register(models.Classification, ClassificationAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Condition, ConditionAdmin)
admin.site.register(models.Material, MaterialAdmin)
admin.site.register(models.Measurement, MeasurementAdmin)
admin.site.register(models.Type, TypeAdmin)
admin.site.register(models.Part, PartAdmin)

accession_admin = admin.AdminSite(name="tfc")
accession_admin.register(models.Accession, AccessionAdmin)
accession_admin.register(models.Donor, DonorAdmin)
accession_admin.register(models.City, CityAdmin)
accession_admin.register(models.Country, CountryAdmin)
accession_admin.register(models.Designer, DesignerAdmin)
accession_admin.register(models.Label, LabelAdmin)
accession_admin.register(models.Retailer, RetailerAdmin)
accession_admin.register(models.Retailer_Label, Retailer_LabelAdmin)
accession_admin.register(models.Classification, ClassificationAdmin)
accession_admin.register(models.Location, LocationAdmin)
accession_admin.register(models.Condition, ConditionAdmin)
accession_admin.register(models.Material, MaterialAdmin)
accession_admin.register(models.Measurement, MeasurementAdmin)
accession_admin.register(models.Type, TypeAdmin)
accession_admin.register(models.Part, PartAdmin)
accession_admin.register(models.Object, ObjectAdmin)
