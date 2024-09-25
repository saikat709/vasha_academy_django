# Generated by Django 5.1.1 on 2024-09-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_coursetype_useranswer'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('questions', models.ManyToManyField(related_name='courses', to='question.question')),
            ],
        ),
    ]
