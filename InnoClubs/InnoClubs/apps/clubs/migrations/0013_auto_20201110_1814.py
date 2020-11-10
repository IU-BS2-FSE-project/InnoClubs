# Generated by Django 3.1.2 on 2020-11-10 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0012_auto_20201110_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clubs.club'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onetimeevent',
            name='club',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clubs.club'),
            preserve_default=False,
        ),
    ]
