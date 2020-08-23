from django.shortcuts import render
from . import models
from track.views import get_track_ctx

# Create your views here.

def song(request, track_name = None, song_name = None):
    ctx = get_track_ctx(track_name)
    ctx = get_song_ctx(ctx, song_name)

    return render(request, 'song.html', ctx)


def get_song_ctx(ctx, song_name=None):
    song = None
    multiple_content = True

    if song_name != None:
        songs = models.Song.objects.filter(friendly_link=song_name, track=ctx["track"])
        if len(songs) == 1:
            song = songs[0]
            multiple_content = False
            ctx["title"] = ("Hudini | " + str(ctx["track"].title) + " - " + str(song.title))
            print(song)
            img = getattr(song, 'image', False)
            ctx["bg_image"] = img if img != None else getattr(ctx["track"], 'image', False)
        else:
            track_link = ctx["track"]["friendly_link"]
            return redirect(f"/track/{track_link}/song")

    if multiple_content:
        song = models.Song.objects.filter(track=ctx["track"])
        song = song.order_by('id_in_track')
        ctx["title"] = ("Hudini | " + str(ctx["track"].title))

    ctx["nav_name"] = str(ctx["track"].title)

    ctx.update({
        "song" : song,
        "multiple_content" : multiple_content,
    })

    return ctx