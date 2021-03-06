# Generated by Django 3.1.2 on 2020-10-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_chat',
            field=models.CharField(max_length=200, null=True, verbose_name='Telegram chat'),
        ),
        migrations.AlterField(
            model_name='club',
            name='club_logo',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
    ]
