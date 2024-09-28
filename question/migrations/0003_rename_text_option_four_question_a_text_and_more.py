# Generated by Django 5.1.1 on 2024-09-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_rename_name_question_question_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text_option_four',
            new_name='a_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text_option_one',
            new_name='b_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text_option_three',
            new_name='c_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text_option_two',
            new_name='d_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image_option_four',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image_option_one',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image_option_three',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image_option_two',
        ),
        migrations.AddField(
            model_name='question',
            name='a_audio',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='question',
            name='a_img',
            field=models.ImageField(blank=True, null=True, upload_to='audios/'),
        ),
        migrations.AddField(
            model_name='question',
            name='b_audio',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='question',
            name='b_img',
            field=models.ImageField(blank=True, null=True, upload_to='audios/'),
        ),
        migrations.AddField(
            model_name='question',
            name='c_audio',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='question',
            name='c_img',
            field=models.ImageField(blank=True, null=True, upload_to='audios/'),
        ),
        migrations.AddField(
            model_name='question',
            name='d_audio',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='question',
            name='d_img',
            field=models.ImageField(blank=True, null=True, upload_to='audios/'),
        ),
    ]
