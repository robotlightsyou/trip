from django.shortcuts import render

# Create your views here.


def users_home(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})
