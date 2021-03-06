# Generated by Django 2.1.2 on 2018-10-23 09:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('T_or_F', models.BooleanField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
