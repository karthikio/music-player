# Generated by Django 3.2.5 on 2021-07-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('song', models.FileField(upload_to='uploads/music/', verbose_name='Song')),
                ('favourite', models.BooleanField(default=False)),
            ],
        ),
    ]
