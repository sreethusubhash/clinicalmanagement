# Generated by Django 4.2.4 on 2023-09-04 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0009_rename_description_resources_descriptions"),
    ]

    operations = [
        migrations.AddField(
            model_name="resources",
            name="dept_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="resources.departments",
            ),
        ),
        migrations.AlterField(
            model_name="resources",
            name="dept_name",
            field=models.CharField(max_length=100),
        ),
    ]
