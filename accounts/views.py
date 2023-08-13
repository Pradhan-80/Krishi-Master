from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse, reverse_lazy

from .forms import *
from .permissions import user_is_student 


def get_success_url(request):

    """
    Handle Success Url After LogIN
    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('jobportal:home')



def student_registration(request):

    """
    Handle student Registration
    """
    form = studentRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context={
        
            'form':form
        }

    return render(request,'main/student-registration.html',context)


def recruiter_registration(request):

    """
    Handle student Registration 
    """

    form = recruiterRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context={
        
            'form':form
        }

    return render(request,'main/recruiter-registration.html',context)


@login_required(login_url=reverse_lazy('accounts:login'))
@user_is_student
def student_edit_profile(request, id=id):

    """
    Handle student Profile Update Functionality
    """

    user = get_object_or_404(User, id=id)
    form = studentProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form = form.save()
        messages.success(request, 'Your Profile Was Successfully Updated!')
        return redirect(reverse("account:edit-profile", kwargs={
                                    'id': form.id
                                    }))
    context={
        
            'form':form
        }

    return render(request,'main/student-edit-profile.html',context)



def user_logIn(request):

    """
    Provides users to logIn
    """

    form = UserLoginForm(request.POST or None)
    

    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_url(request))
    context = {
        'form': form,
    }

    return render(request,'main/login.html',context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')