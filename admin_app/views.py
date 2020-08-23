from django.shortcuts import render, redirect
from . import forms
import homepage

# Create your views here.

def Home(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect("signup")


def signup(request):
    ctx = homepage.views.base_context()
    ctx["title"] = "Hudini | Zarejestruj"
    ctx["nav_name"] = "--"
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    ctx.update({"form":form})
    return render(request, 'signup.html', ctx)