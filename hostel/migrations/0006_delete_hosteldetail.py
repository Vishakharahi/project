# Generated by Django 4.1.4 on 2022-12-28 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_remove_hosteldetail_contact_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HostelDetail',
        ),
    ]
