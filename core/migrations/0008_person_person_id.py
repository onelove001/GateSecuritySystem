# Generated by Django 3.1.4 on 2022-07-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220712_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_id',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
