# Generated by Django 4.1 on 2023-08-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Category", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_id",
            field=models.AutoField(default=" ", primary_key=True, serialize=False),
        ),
    ]
