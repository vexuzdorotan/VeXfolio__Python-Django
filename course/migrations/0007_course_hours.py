# Generated by Django 3.0.3 on 2020-08-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_show_to_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='hours',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
