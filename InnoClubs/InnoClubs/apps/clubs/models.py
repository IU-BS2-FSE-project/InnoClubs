from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Club(models.Model):
    club_title = models.CharField("Title of the club", max_length=200, editable=False)
    club_info = models.CharField("Information of the club", max_length=2000)
    club_logo = models.ImageField(upload_to="static/img/", null=True)
    club_url = models.CharField(
        "Url of the club(For example testUrl)", max_length=200, editable=False)
    club_chat = models.CharField("Telegram chat", max_length=200, null=True)

    def __str__(self):
        return self.club_title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hours = models.TimeField("Hours", null=True, blank=True)
    # how to use info from ManyToManyField - https://metanit.com/python/django/5.7.php
    subscriptions = models.ManyToManyField(Club, blank=True)

    def __str__(self):
        return self.user.username


class ClubAdmin(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    rights = models.CharField("Rights", max_length=9)

    def __str__(self):
        return self.club.club_title + " " + self.student.user.username


class News(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=32)
    info = models.TextField("Info", null=True, blank=True)
    publication_date = models.DateTimeField("Publication_date", auto_now_add=True)
    due_date = models.DateField("Due_date", null=True, blank=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    CHOICES = (
        (6, 'Sunday'),
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
    )
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    text = models.TextField()
    week_day = models.IntegerField(choices=CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=16)
    participants = models.ManyToManyField(Student, blank=True)
    img = models.ImageField(upload_to="static/img/events", null=True)

    def __str__(self):
        return self.title


class OneTimeEvent(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    text = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=15)
    participants = models.ManyToManyField(Student, blank=True)
    img = models.ImageField(upload_to="static/img/events", null=True)

    def __str__(self):
        return self.title


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


class Attendance(models.Model):     # it should not be here, but I cant connect it in other app
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField("date", auto_now_add=True, editable=False, null=False, blank=False)
    attended = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return str(self.date) + " " + str(self.event)
