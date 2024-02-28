# Generated by Django 5.0.2 on 2024-02-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="catalog.actor"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="directors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="catalog.director"
            ),
        ),
    ]
