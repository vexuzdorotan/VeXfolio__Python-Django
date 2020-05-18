# Generated by Django 3.0.3 on 2020-05-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='portfolio')),
                ('link', models.URLField(blank=True)),
                ('date_added', models.DateField()),
                ('show', models.BooleanField(default=False)),
            ],
        ),
    ]