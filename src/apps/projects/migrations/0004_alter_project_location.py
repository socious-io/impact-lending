# Generated by Django 4.2.1 on 2023-06-06 09:17

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='location',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]