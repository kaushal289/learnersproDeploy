# Generated by Django 4.0 on 2022-05-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('student_firstname', models.CharField(max_length=100)),
                ('student_lastname', models.CharField(max_length=200)),
                ('student_username', models.CharField(max_length=100)),
                ('stuent_number', models.CharField(max_length=10)),
                ('student_email', models.CharField(max_length=100)),
                ('customer_password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
