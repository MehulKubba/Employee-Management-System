# Generated by Django 4.2.9 on 2024-01-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emp_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="id",
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]