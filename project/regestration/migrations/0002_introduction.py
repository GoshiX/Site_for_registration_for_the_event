# Generated by Django 3.2.7 on 2021-11-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regestration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(upload_to='')),
                ('Title', models.TextField()),
                ('Start_date', models.DateField()),
                ('Start_time', models.TimeField()),
                ('Info', models.TextField()),
            ],
        ),
    ]
