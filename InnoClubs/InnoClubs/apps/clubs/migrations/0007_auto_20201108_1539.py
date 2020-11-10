# Generated by Django 3.1.2 on 2020-11-08 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_auto_20201108_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.club'),
        ),
        migrations.AlterField(
            model_name='news',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Due_date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Publication_date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Title'),
        ),
    ]