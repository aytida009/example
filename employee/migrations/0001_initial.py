# Generated by Django 3.2.9 on 2022-02-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
        ),
    ]