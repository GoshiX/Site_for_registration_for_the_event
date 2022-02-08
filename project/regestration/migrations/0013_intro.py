# Generated by Django 3.2.7 on 2022-02-08 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regestration', '0012_auto_20220208_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bc_img', models.ImageField(upload_to='templates/image')),
                ('title', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('text', models.TextField()),
                ('text_color', models.TextField(default='#000000')),
                ('block_color', models.TextField(default='#000000')),
                ('model_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regestration.description')),
            ],
        ),
    ]
