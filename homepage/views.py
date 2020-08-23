from django.shortcuts import render, redirect
from . import models
from django.template import RequestContext

# Create your views here.

def Homepage(request):

    try:
        return redirect("/track/fragmenty")
        pass
    except:
        pass
        return render(request, "pages/homepage.html", base_context())

def Not_found(request):
    return render(request, "pages/not_found.html", base_context())

def base_context():
    from track.models import Track
    external = models.ExternalLink.objects.all()
    all_tracks = Track.objects.all()
    ctx = {
        "title" : "Hudini",
        "external_links" : external,
        "nav_name" : "Home",
        "all_tracks" : all_tracks,
        "bg_image" : None
    }
    return ctx



def handler404(request, *args, **argv):
    return  render(request, 'pages/not_found.html', base_context())


def handler500(request, *args, **argv):
    return  render(request, 'pages/not_found.html', base_context())