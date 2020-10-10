from django.db import models


class Participant(models.Model):  # I want to change this name. Not User. Wait for your ideas
    login = models.CharField('login', max_length=64)
    name = models.CharField('name', max_length=32)
    sname = models.CharField('surname', max_length=32)
    mail = models.EmailField('e.mail', max_length=64)
    password = models.CharField('password', max_length=64)  # TODO create new Field for password if possible
    hours = models.DecimalField('hours/semestr', max_digits=5,
                                decimal_places=2)  # maybe it is too early for this field
