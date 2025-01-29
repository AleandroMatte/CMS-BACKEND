# Generated by Django 5.1.5 on 2025-01-29 01:15

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Component",
            fields=[
                (
                    "shared_id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "component_type",
                    models.CharField(
                        choices=[
                            ("TEXT", "Text"),
                            ("IMAGE", "Image"),
                            ("TITLE", "Title"),
                            ("SNIPPET", "Snippet"),
                            ("VIDEO", "Video"),
                        ],
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("updated_at", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
