# Generated by Django 4.2.4 on 2023-09-30 14:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0003_rename_phone_name_registration_phone_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="registration",
            options={"verbose_name_plural": "Registration"},
        ),
    ]
