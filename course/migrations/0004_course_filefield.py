# Generated by Django 5.1.1 on 2024-09-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='filefield',
            field=models.FileField(default=None, upload_to='course/'),
            preserve_default=False,
        ),
    ]