# Generated by Django 4.1.4 on 2023-04-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("film", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActorModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="Enter your name", max_length=150)),
                (
                    "surname",
                    models.CharField(help_text="Enter your surname", max_length=150),
                ),
                ("age", models.IntegerField(blank=True, null=True)),
                ("about", models.TextField(blank=True, null=True)),
                (
                    "films",
                    models.ManyToManyField(related_name="actors", to="film.filmmodel"),
                ),
            ],
            options={"verbose_name": "Actor",},
        ),
    ]
