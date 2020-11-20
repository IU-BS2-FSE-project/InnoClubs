from django.db import models


# Create your models here.

class Club(models.Model):
    club_title = models.CharField("Title of the club", max_length=200)
    club_info = models.CharField("Information of the club", max_length=2000)
    club_logo = models.ImageField(
        upload_to="static/img/",
        null=False,
        default="static/img/no_image_found.png")
    club_url = models.CharField(
        "Url of the club(For example testUrl)", max_length=200)
    club_chat = models.CharField("Telegram chat", max_length=200, null=True)

    def __str__(self):
        return self.club_title


class ClubType(models.Model):
    type_name = models.CharField("Title of the type", max_length=255)
    type_image = models.ImageField(upload_to="static/img", null=True)
    # TODO: remove null and add 404 page as default one
    type_url = models.CharField(
        "Url to the page with list of clubs of "
        "such type (For example testUrl)", max_length=255, null=True)

    def __str__(self):
        return self.type_name
