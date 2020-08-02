# Generated by Django 3.0.6 on 2020-07-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_portfolio_show_to_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rank', models.IntegerField(blank=True)),
                ('show', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='technology',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='percent',
        ),
        migrations.AlterField(
            model_name='technology',
            name='rank',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]