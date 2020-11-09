from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from .forms import AddNewsForm, AddEventForm
from .models import Club, Student, ClubAdmin, News, ClubType
from django.http import HttpResponseRedirect


# if user is not logged in => redirect to the auth/
# if user is logged in => show main page
# args['infoFromDb'] = .... means that we add information of all the clubs
# from database to the args
def main(request):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
        try:
            args['infoFromDb'] = Club.objects.all()
        except ObjectDoesNotExist:
            args['infoFromDb'] = None

        try:
            args['clubTypeList'] = ClubType.objects.all()
        except ObjectDoesNotExist:
            args['clubTypeList'] = None

        return render(request, "clubs/main.html", args)
    else:
        return redirect("auth/")


# if user is not logged in => redirect to the auth/
# if user is logged in => show main page

# args['infoFromDb'] = Club.objects.get(club_url=club_url) means that we add
# information of the exactly one club that was accessed

def ClubPage(request, club_url):
    args = {}
    if auth.get_user(request):
        user = auth.get_user(request)
        club = Club.objects.get(club_url=club_url)
        for record in club.clubadmin_set.all():
            if record.student == user.student:
                args['rights'] = record.rights
        args['user'] = user
        args['club'] = club

        return render(request, "clubs/pageOfClub.html", args)
    else:
        return redirect('auth/')


def subscribe(request, club_url):
    user = auth.get_user(request)
    club = Club.objects.get(club_url=club_url)
    user.student.subscriptions.add(club)
    return HttpResponseRedirect(reverse('clubPage', args=(club_url,)))  # almost same as redirect


def unsubscribe(request, club_url):
    user = auth.get_user(request)
    club = Club.objects.get(club_url=club_url)
    user.student.subscriptions.remove(club)
    return HttpResponseRedirect(reverse('clubPage', args=(club_url,)))


def administration(request, club_url):
    args = {}
    club = Club.objects.get(club_url=club_url)
    args['user'] = auth.get_user(request)
    args['club'] = club
    args['students'] = Student.objects.filter(subscriptions__club_url=club_url)
    admins_list = []
    for record in club.clubadmin_set.all():
        admins_list.append(record.student)
    args['admins_list'] = admins_list

    return render(request, "clubs/administrationOfClub.html", args)


def deleteNews(request, club_url, article_id):
    article = News.objects.get(id=article_id)
    article.delete()
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))


def addNews(request, club_url):
    args = {}
    if request.method == "POST":
        form = AddNewsForm(request.POST)
        if form.is_valid():
            args['form'] = form

            new = form.save(commit=False)
            new.club = Club.objects.get(club_url=club_url)
            new.save()
            return HttpResponseRedirect(reverse('addNews', args=(club_url,)))
        else:
            return render(request, 'clubs/addNews.html', args)
    else:
        form = AddNewsForm()
        args['form'] = form
        return render(request, 'clubs/addNews.html', args)


def addEvent(request, club_url):
    args = {}
    if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            args['form'] = form

            new = form.save(commit=False)
            new.club = Club.objects.get(club_url=club_url)
            new.save()
            return HttpResponseRedirect(reverse('addEvent', args=(club_url,)))
        else:
            return render(request, 'clubs/addEvent.html', args)
    else:
        form = AddEventForm()
        args['form'] = form
        return render(request, 'clubs/addEvent.html', args)


def clubTypes(request):
    args = {}
    args['username'] = auth.get_user(request).username
    try:
        args['clubs'] = Club.objects.all()
    except ObjectDoesNotExist:
        args['clubs'] = None

    return render(request, "clubs/clubTypes.html", args)


def set_assistant(request, club_url, person_id):
    admin = ClubAdmin()
    admin.student = Student.objects.get(id=person_id)
    admin.club = Club.objects.get(club_url=club_url)
    admin.rights = "Assistant"
    admin.save()
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))


def downgrade(request, club_url, admin_id):
    admin = ClubAdmin(id=admin_id)
    if admin.rights == "Assistant":
        admin.delete()
    elif admin.rights == "Admin":
        admin.rights = "Assistant"
        admin.save()
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))
