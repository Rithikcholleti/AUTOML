# Generated by Django 2.0.13 on 2020-07-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_automldatamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPredectionsModels',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('YearsExperience', models.FloatField(default=0)),
                ('Salary', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'mypredections',
            },
        ),
    ]
