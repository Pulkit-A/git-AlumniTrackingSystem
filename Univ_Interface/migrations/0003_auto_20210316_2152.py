# Generated by Django 3.1.4 on 2021-03-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univ_Interface', '0002_eventinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='img',
            field=models.ImageField(blank=True, default='defaultevent.png', null=True, upload_to=''),
        ),
    ]
