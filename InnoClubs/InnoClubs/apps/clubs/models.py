from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Club(models.Model):
    club_title = models.CharField("Title of the club", max_length=200)
    club_info = models.CharField("Information of the club", max_length=2000)
    club_logo = models.ImageField(upload_to="static/img/", null=True)
    club_url = models.CharField(
        "Url of the club(For example testUrl)", max_length=200)
    club_chat = models.CharField("Telegram chat", max_length=200, null=True)

    def __str__(self):
        return self.club_title



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hours = models.TimeField("Hours", null=True, blank=True)
    # how to use info from this field - https://metanit.com/python/django/5.7.php
    subscriptions = models.ManyToManyField(Club, blank=True)


class ClubAdmin(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    rights = models.CharField("Rights", max_length=9)


class News(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=32)
    info = models.TextField("Info", null=True, blank=True)
    publication_date = models.DateTimeField("Publication_date", auto_now_add=True)
    due_date = models.DateField("Due_date")


class Event(models.Model):
    CHOICES = (
        ('Sun.', 'Sunday'),
        ('Mon.', 'Monday'),
        ('Tues.', 'Tuesday'),
        ('Wed.', 'Wednesday'),
        ('Thur.', 'Thursday'),
        ('Fri.', 'Friday'),
        ('Sat.', 'Saturday'),
    )
    week_day = models.CharField(max_length=8, choices=CHOICES, null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=15)
    text = models.TextField()
    one_time = models.BooleanField(default=False)


class OneTimeEvent(models.Model):
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=15)
    text = models.TextField()


# these two methods need for adding default Users records to custom Student
# link to method https://habr.com/ru/post/313764/#OneToOneField
# Note: if you want to use data from Student, f.e. hours, you should write user.student.hours
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()


class ClubType(models.Model):
    type_name = models.CharField("Title of the type", max_length=255)
    type_image = models.ImageField(upload_to="static/img", null=True)
    # TODO: remove null and add 404 page as default one
    type_url = models.CharField(
        "Url to the page with list of clubs of "
        "such type (For example testUrl)", max_length=255, null=True)

    def __str__(self):
        return self.type_name

