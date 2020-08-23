from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from . import models
import homepage

# Create your views here.

def track_page(request, track_name=None):
    return render(request, "track.html", get_track_ctx(track_name))

def get_track_ctx(track_name=None):
    track = None
    multiple_content = True
    ctx = homepage.views.base_context()

    if track_name != None:
        tracks = models.Track.objects.filter(friendly_link=track_name)
        if len(tracks) == 1:
            track = tracks[0]
            multiple_content = False
            ctx["title"] = ("Hudini | " + str(track.title))
            ctx["nav_name"] = str(track.title)
            ctx["bg_image"] = track.bg_image
        else:
            return redirect("/track")

    if multiple_content:
        track = models.Track.objects.all()
        ctx["title"] = ("Hudini | albumy")
        ctx["nav_name"] = "Albumy"

    ctx.update({
        "track" : track,
        "multiple_content" : multiple_content,
    })

    return ctx