# Generated by Django 2.1.1 on 2018-11-05 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseoverview',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
