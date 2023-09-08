from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import Profile
from accounts.forms import UserRegistrationForm, UserEditForm, ProfileEditForm


# Create your views here.

@login_required
def dashboard(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
    return render(request,
                  'accounts/account/dashboard.html',
                  {'section': 'account'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
        return render(request,
                      'accounts/account/register_done.html',
                      {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/account/register.html', {'user_form': user_form})


# 회원 정보 수정
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'accounts/account/profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
