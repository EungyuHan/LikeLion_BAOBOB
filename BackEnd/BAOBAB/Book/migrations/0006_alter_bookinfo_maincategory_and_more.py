# Generated by Django 4.1 on 2023-08-01 11:04

import Book.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Category", "0005_category_category_id_alter_category_category_name"),
        ("Book", "0005_rename_rating_bookstats_average_rating_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinfo",
            name="mainCategory",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="mainCategory",
                to="Category.category",
                validators=[Book.models.main_category_validator],
            ),
        ),
        migrations.AlterField(
            model_name="bookinfo",
            name="subCategory",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="subCategory",
                to="Category.category",
                validators=[Book.models.sub_category_validator],
            ),
        ),
    ]
