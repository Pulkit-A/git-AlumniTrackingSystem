# Generated by Django 3.1.4 on 2021-01-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniinfo',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
