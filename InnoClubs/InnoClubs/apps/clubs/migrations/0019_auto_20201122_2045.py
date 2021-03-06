# Generated by Django 3.1.2 on 2020-11-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0018_merge_20201122_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_logo',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='club',
            name='club_url',
            field=models.CharField(max_length=200, verbose_name='Url of the club(For example testUrl)'),
        ),
    ]
