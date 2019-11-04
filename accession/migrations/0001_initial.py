# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accession_number', models.CharField(unique=True, max_length=12)),
                ('date_received', models.DateField(null=True, blank=True)),
                ('description', models.TextField(help_text=b'Publicly viewable description of the accession')),
                ('date_in_computer', models.DateField(null=True, blank=True)),
                ('acquisition_method', models.CharField(default=b'GIK', max_length=3, choices=[(b'GIK', b'Gift In Kind'), (b'TRN', b'Transfer'), (b'PUR', b'Purchase'), (b'OTH', b'Other')])),
                ('anonymous_accession', models.BooleanField(help_text=b'Check if accession should be listed as anonymous on any public interface')),
                ('date_paperwork_sent', models.DateField(help_text=b'Date recipt of gift (ROG) was mailed out', null=True, blank=True)),
                ('date_paperwork_returned', models.DateField(help_text=b'Date signed recipt of gift (ROG) was received', null=True, blank=True)),
                ('accession_note', models.TextField(help_text=b'Private note related to this accession', blank=True)),
            ],
            options={
                'ordering': ['accession_number'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ['city'],
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classification', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['classification'],
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['condition'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['country'],
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designer', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['designer'],
            },
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salutation', models.CharField(blank=True, max_length=5, choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MISS', b'Miss'), (b'MS', b'Ms.'), (b'MRMRS', b'Mr. and Mrs.'), (b'DR', b'Dr.')])),
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('middle_name', models.CharField(max_length=100, blank=True)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('organization_name', models.CharField(max_length=255, blank=True)),
                ('donor_type', models.CharField(default=b'PER', max_length=3, blank=True, choices=[(b'PER', b'Person'), (b'ORG', b'Organization')])),
                ('gender', models.CharField(blank=True, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address_1', models.CharField(max_length=100, blank=True)),
                ('address_2', models.CharField(max_length=100, blank=True)),
                ('state', models.CharField(blank=True, max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('postal_code', models.CharField(max_length=15, blank=True)),
                ('phone_number_1', models.CharField(help_text=b'Please use the following format: <em>(940) 391-0414</em>.', max_length=25, blank=True)),
                ('phone_number_2', models.CharField(help_text=b'Please use the following format: <em>(940) 391-0414</em>.', max_length=25, blank=True)),
                ('email_address', models.EmailField(max_length=254, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('city', models.ForeignKey(blank=True, to='accession.City', null=True)),
                ('country', models.ForeignKey(blank=True, to='accession.Country', null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200, verbose_name=b'Designer Label')),
            ],
            options={
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['location'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('measurement', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['measurement'],
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_number', models.CharField(max_length=20)),
                ('object_description', models.TextField()),
                ('related_objects', models.CharField(max_length=200, blank=True)),
                ('original_numbers', models.CharField(max_length=100, blank=True)),
                ('date_object_creation', models.CharField(max_length=100, blank=True)),
                ('object_era', models.CharField(blank=True, max_length=10, choices=[(b'Pre-1770', b'Pre-1770'), (b'1770-1779', b'1770-1779'), (b'1780-1789', b'1780-1789'), (b'1790-1799', b'1790-1799'), (b'1800-1809', b'1800-1809'), (b'1810-1819', b'1810-1819'), (b'1820-1829', b'1820-1829'), (b'1830-1839', b'1830-1839'), (b'1840-1849', b'1840-1849'), (b'1850-1859', b'1850-1859'), (b'1860-1869', b'1860-1869'), (b'1870-1879', b'1870-1879'), (b'1880-1889', b'1880-1889'), (b'1890-1899', b'1890-1899'), (b'1900-1909', b'1900-1909'), (b'1910-1919', b'1910-1919'), (b'1920-1929', b'1920-1929'), (b'1930-1939', b'1930-1939'), (b'1940-1949', b'1940-1949'), (b'1950-1959', b'1950-1959'), (b'1960-1969', b'1960-1969'), (b'1970-1979', b'1970-1979'), (b'1980-1989', b'1980-1989'), (b'1990-1999', b'1990-1999'), (b'2000-2009', b'2000-2009'), (b'2010-2019', b'2010-2019')])),
                ('remarks', models.TextField(blank=True)),
                ('location_remarks', models.TextField(blank=True)),
                ('construction', models.TextField(blank=True)),
                ('exhibitions', models.TextField(blank=True)),
                ('publications', models.TextField(blank=True)),
                ('provenance', models.TextField(blank=True)),
                ('condition_statement', models.TextField(blank=True)),
                ('price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('public_notes', models.TextField(blank=True)),
                ('gender', models.CharField(max_length=14, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'U', b'Unisex'), (b'UnKn', b'Gender Unknown'), (b'UnRec', b'Not Recorded'), (b'NA', b'Not Applicable')])),
                ('date_record_added', models.DateTimeField(auto_now_add=True)),
                ('date_record_last_edited', models.DateTimeField(auto_now=True)),
                ('accession_number', models.ForeignKey(to='accession.Accession')),
                ('classification', models.ForeignKey(to='accession.Classification')),
                ('condition', models.ForeignKey(to='accession.Condition')),
                ('country', models.ForeignKey(blank=True, to='accession.Country', null=True)),
                ('designer', models.ForeignKey(blank=True, to='accession.Designer', null=True)),
                ('label', models.ForeignKey(verbose_name=b'Designer Label', blank=True, to='accession.Label', null=True)),
                ('location', models.ForeignKey(to='accession.Location')),
                ('material', models.ForeignKey(blank=True, to='accession.Material', null=True)),
                ('measurement', models.ForeignKey(blank=True, to='accession.Measurement', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['part'],
            },
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('retailer_name', models.CharField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ['retailer_name'],
            },
        ),
        migrations.CreateModel(
            name='Retailer_Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('retailer_label', models.CharField(unique=True, max_length=200, verbose_name=b'Retailer Label')),
            ],
            options={
                'ordering': ['retailer_label'],
                'verbose_name_plural': 'Retailer Labels',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_type', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['object_type'],
            },
        ),
        migrations.AddField(
            model_name='object',
            name='parts',
            field=models.ForeignKey(blank=True, to='accession.Part', null=True),
        ),
        migrations.AddField(
            model_name='object',
            name='retailer',
            field=models.ForeignKey(blank=True, to='accession.Retailer', null=True),
        ),
        migrations.AddField(
            model_name='object',
            name='retailer_label',
            field=models.ForeignKey(verbose_name=b'Retailer Label', blank=True, to='accession.Retailer_Label', null=True),
        ),
        migrations.AddField(
            model_name='object',
            name='type',
            field=models.ForeignKey(blank=True, to='accession.Type', null=True),
        ),
        migrations.AddField(
            model_name='accession',
            name='donor',
            field=models.ForeignKey(to='accession.Donor'),
        ),
    ]
