# Generated by Django 5.1.3 on 2024-12-16 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicalprofessional",
            name="departments",
            field=models.ManyToManyField(
                related_name="professionals", to="api.department"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="primary_hospital",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.hospital",
            ),
        ),
    ]