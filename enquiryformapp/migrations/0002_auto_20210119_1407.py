# Generated by Django 3.0 on 2021-01-19 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryformapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry_data',
            old_name='start_data',
            new_name='start_date',
        ),
    ]
