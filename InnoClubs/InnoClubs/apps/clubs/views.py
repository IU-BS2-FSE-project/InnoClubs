from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

from django.urls import reverse
from .forms import AddNewsForm, AddEventForm, ClubInfoChangeForm, AddOneTimeEventForm
from .models import Club, Student, ClubAdmin, News, ClubType, Event, OneTimeEvent
from django.http import HttpResponseRedirect



# if user is not logged in => redirect to the auth/
# if user is logged in => show main page
# args['infoFromDb'] = .... means that we add information of all the clubs
# from database to the args
def main(request):
    args = {}
    if auth.get_user(request).username:
        args['user'] = auth.get_user(request)
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
    user = auth.get_user(request)
    args['user'] = user
    args['club'] = club
    args['students'] = Student.objects.filter(subscriptions__club_url=club_url)
    isAdmin = ClubAdmin.objects.get(club=club, student=user.student)
    admins_list = []
    for record in club.clubadmin_set.all():
        admins_list.append(record.student)
    args['admins_list'] = admins_list
    if isAdmin.rights == "Admin":
        if request.method == "POST":
            form = ClubInfoChangeForm(request.POST, request.FILES)
            if form.is_valid():
                updates = form.save(commit=False)
                club.club_info = updates.club_info
                if updates.club_logo:
                    club.club_logo = updates.club_logo
                club.club_chat = updates.club_chat
                club.save()
                return HttpResponseRedirect(reverse('administration', args=(club_url,)))
            else:
                args['form'] = form
                return render(request, 'clubs/administrationOfClub.html', args)
        else:
            form = ClubInfoChangeForm(initial={'club_info': club.club_info,
                                               'club_chat': club.club_chat,
                                               'club_logo': club.club_logo})
            args['form'] = form
            return render(request, 'clubs/administrationOfClub.html', args)
    else:
        return redirect('/')


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


def add_event(request, club_url):
    args = {}
    if request.method == "POST":
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            args['form'] = form

            event = form.save(commit=False)
            event.club = Club.objects.get(club_url=club_url)
            event.save()
            return HttpResponseRedirect(reverse('add_event', args=(club_url, )))
        else:
            return render(request, 'clubs/addEvent.html', args)
    else:
        form = AddEventForm()
        args['form'] = form
        return render(request, 'clubs/addEvent.html', args)


def add_one_time_event(request, club_url):
    args = {}
    if request.method == "POST":
        form = AddOneTimeEventForm(request.POST, request.FILES)
        if form.is_valid():
            args['form'] = form

            event = form.save(commit=False)
            event.club = Club.objects.get(club_url=club_url)
            event.save()
            return HttpResponseRedirect(reverse('add_one_time_event', args=(club_url,)))
        else:
            return render(request, 'clubs/addOneTimeEvent.html', args)
    else:
        form = AddOneTimeEventForm()
        args['form'] = form
        return render(request, 'clubs/addOneTimeEvent.html', args)


def clubTypes(request,type_url):
    args = {}
    args['username'] = auth.get_user(request).username
    try:
        neededType = ClubType.objects.get(type_url=type_url)
        args['currentType'] = neededType
        args['clubs'] = Club.objects.all().filter(club_type=neededType)
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
    admin = ClubAdmin.objects.get(id=admin_id)
    if admin.rights == "Assistant":
        admin.delete()
    elif admin.rights == "Admin":
        admin.rights = "Assistant"
        admin.save()
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))


def set_admin(request, club_url, admin_id):
    admin = ClubAdmin.objects.get(id=admin_id)
    if admin.rights == "Assistant":
        admin.rights = "Admin"
        admin.save()
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))


def kick(request, club_url, person_id):
    club = Club.objects.get(club_url=club_url)
    club.student_set.remove(person_id)
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))


def del_event(request, club_url, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))


def del_otevent(request, club_url, event_id):
    event = OneTimeEvent.objects.get(id=event_id)
    event.delete()
    return HttpResponseRedirect(reverse('administration', args=(club_url,)))
