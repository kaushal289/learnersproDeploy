# Generated by Django 4.0 on 2022-07-02 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
            preserve_default=False,
        ),
    ]
