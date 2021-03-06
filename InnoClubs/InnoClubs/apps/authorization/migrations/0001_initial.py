# Generated by Django 3.1.2 on 2020-10-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=64, verbose_name='login')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('sname', models.CharField(max_length=32, verbose_name='surname')),
                ('mail', models.EmailField(max_length=64, verbose_name='e.mail')),
                ('password', models.CharField(max_length=64, verbose_name='password')),
                ('hours', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='hours/semestr')),
            ],
        ),
    ]
