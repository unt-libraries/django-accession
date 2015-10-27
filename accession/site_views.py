from django.contrib import admin
import django_databrowse as databrowse
#Accession Models
from accession.models import Accession, Donor, Country, Designer, \
Label, Classification, Condition, Material, Measurement, \
Type, Part, Object, Retailer, Retailer_Label
from accession.models import Location as accession_Location
from accession.models import Country as accession_Country
from accession.models import City as accession_City
#Accession Admins
from accession.admin import AccessionAdmin, DonorAdmin, ObjectAdmin, \
DesignerAdmin, LabelAdmin, ClassificationAdmin, \
ConditionAdmin, MaterialAdmin, MeasurementAdmin, \
TypeAdmin, PartAdmin, RetailerAdmin, Retailer_LabelAdmin
from accession.admin import LocationAdmin as accession_LocationAdmin
from accession.admin import CountryAdmin as accession_CountryAdmin
from accession.admin import CityAdmin as accession_CityAdmin
#Register all the admin objects that live in the main admin
main_admin = admin.AdminSite(name="main")
#Accession
main_admin.register(Accession, AccessionAdmin)
main_admin.register(Donor, DonorAdmin)
main_admin.register(Object, ObjectAdmin)
main_admin.register(accession_City, accession_CityAdmin)
main_admin.register(accession_Country, accession_CountryAdmin)
main_admin.register(Designer, DesignerAdmin)
main_admin.register(Label, LabelAdmin)
main_admin.register(Retailer, RetailerAdmin)
main_admin.register(Retailer_Label, Retailer_LabelAdmin)
main_admin.register(Classification, ClassificationAdmin)
main_admin.register(accession_Location, accession_LocationAdmin)
main_admin.register(Condition, ConditionAdmin)
main_admin.register(Material, MaterialAdmin)
main_admin.register(Measurement, MeasurementAdmin)
main_admin.register(Type, TypeAdmin)
main_admin.register(Part, PartAdmin)
#Register all the admin objects that live under accession
accession_admin = admin.AdminSite(name="tfc")
accession_admin.register(Accession, AccessionAdmin)
accession_admin.register(Donor, DonorAdmin)
accession_admin.register(accession_City, accession_CityAdmin)
accession_admin.register(accession_Country, accession_CountryAdmin)
accession_admin.register(Designer, DesignerAdmin)
accession_admin.register(Label, LabelAdmin)
accession_admin.register(Retailer, RetailerAdmin)
accession_admin.register(Retailer_Label, Retailer_LabelAdmin)
accession_admin.register(Classification, ClassificationAdmin)
accession_admin.register(accession_Location, accession_LocationAdmin)
accession_admin.register(Condition, ConditionAdmin)
accession_admin.register(Material, MaterialAdmin)
accession_admin.register(Measurement, MeasurementAdmin)
accession_admin.register(Type, TypeAdmin)
accession_admin.register(Part, PartAdmin)
accession_admin.register(Object, ObjectAdmin)

#Databrowse for accession
databrowse.site.register(Accession)
databrowse.site.register(Donor)
databrowse.site.register(accession_City)
databrowse.site.register(accession_Country)
databrowse.site.register(Designer)
databrowse.site.register(Label)
databrowse.site.register(Retailer)
databrowse.site.register(Retailer_Label)
databrowse.site.register(Classification)
databrowse.site.register(accession_Location)
databrowse.site.register(Condition)
databrowse.site.register(Material)
databrowse.site.register(Measurement)
databrowse.site.register(Type)
databrowse.site.register(Part)
databrowse.site.register(Object)
