# Generated by Django 3.1.4 on 2022-07-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_person_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]