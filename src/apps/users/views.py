# from requests import post
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request=request)

        if not form.is_valid():
            return render(request, 'update_profile.html', {'form': form}, status=400)

        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.country = form.cleaned_data['country']
        user.save()
        return render(request, 'update_profile.html', {'form': form})

    form = ProfileForm(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'country': user.country
    })

    return render(request, 'update_profile.html', {'form': form})
