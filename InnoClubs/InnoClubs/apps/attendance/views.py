import random

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime
from django.apps import apps
Club = apps.get_model('clubs', 'Club')
Event = apps.get_model('clubs', 'Event')
OneTimeEvent = apps.get_model('clubs', 'OneTimeEvent')
Student = apps.get_model('clubs', 'Student')
Attendance = apps.get_model('clubs', 'Attendance')
ClubAdmin = apps.get_model('clubs', 'ClubAdmin')
codes = {}


def profile(request):
    args = {}
    # example data
    args['user'] = auth.get_user(request)
    return render(request, "attendance/profile.html", args)


def events_list(request, club_url):
    args = {}
    club = Club.objects.get(club_url=club_url)
    events = Event.objects.filter(club=club)
    ot_events = OneTimeEvent.objects.filter(club=club)
    user = auth.get_user(request)
    list_event = []
    list_otevent = []
    for event in events:
        if is_ready(event, False):
            list_event.append(event)
    for event in ot_events:
        if is_ready(event, True):
            list_otevent.append(event)

    args['user'] = user
    args['club'] = club
    args['events'] = list_event
    args['ot_events'] = list_otevent
    args['date'] = datetime.datetime.today()
    return render(request, "attendance/events_list.html", args)


def is_ready(event, is_one_time):
    if is_one_time:
        if event.date != datetime.datetime.today():
            return False
    else:
        if event.week_day != datetime.datetime.today().weekday():
            return False
    now = datetime.datetime.now().time()
    time_delta = abs((event.start_time.hour - now.hour)*3600 +
                     (event.start_time.minute - now.minute)*60 +
                     (event.start_time.second - now.second))
    if (time_delta/60) > 30:    # it is possible to change borders here
        return False
    return True


def check_attendance(request, club_url, event_id):
    args = {}
    club = Club.objects.get(club_url=club_url)
    user = auth.get_user(request)
    try:
        ClubAdmin.objects.get(club=club, student=user.student)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('view_code', args=(club_url, event_id)))

    event = Event.objects.get(id=event_id)
    try:
        attendance = Attendance.objects.get(event=event_id, date__date=datetime.date.today())
    except ObjectDoesNotExist:
        attendance = Attendance.objects.create(event=event, date=datetime.datetime.now())
        attendance.save()

    args['user'] = user
    args['club'] = club
    args['attendance'] = attendance
    args['time'] = datetime.date.today()
    try:
        if request.method == "POST":
            code = request.POST.get("code")
            attended_user = codes.get(int(code))
            attendance.attended.add(attended_user.student)
            args['check'] = attended_user
        return render(request, "attendance/check_attendance.html", args)
    except AttributeError:
        return render(request, "attendance/check_attendance.html", args)


def check_attendance(request, club_url, event_id):
    args = {}
    club = Club.objects.get(club_url=club_url)
    user = auth.get_user(request)
    try:
        ClubAdmin.objects.get(club=club, student=user.student)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('view_code', args=(club_url, event_id)))

    event = Event.objects.get(id=event_id)
    try:
        attendance = Attendance.objects.get(event=event_id, date__date=datetime.date.today())
    except ObjectDoesNotExist:
        attendance = Attendance.objects.create(event=event, date=datetime.datetime.now())
        attendance.save()

    args['user'] = user
    args['club'] = club
    args['attendance'] = attendance
    args['time'] = datetime.date.today()
    try:
        if request.method == "POST":
            code = request.POST.get("code")
            attended_user = codes.get(int(code))
            attendance.attended.add(attended_user.student)
            args['check'] = attended_user
        return render(request, "attendance/check_attendance.html", args)
    except AttributeError:
        return render(request, "attendance/check_attendance.html", args)


def view_code(request, club_url, event_id):
    args = {}
    club = Club.objects.get(club_url=club_url)
    user = auth.get_user(request)
    code = random.randint(100000, 999999)
    args['code'] = code
    codes[code] = user
    args['user'] = user
    args['club'] = club
    args['check'] = datetime.date.today()
    return render(request, "attendance/code.html", args)
