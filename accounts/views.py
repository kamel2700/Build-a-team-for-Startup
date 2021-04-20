from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from accounts.forms import RegistrationForm, EditProfileForm, ProfileUpdateForm, ProjectCreateForm, EditProjectForm, \
    AddCommentForm
from accounts.models import ProjectPage, UserProfile, Comment



def home(request):
    args = {'user': request.user}
    return render(request, 'accounts/home.html', args)


def login_redirect(request):
    return redirect('account/')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../login')
        else:
            args = {'form': form}
            return render(request, 'accounts/registration.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/registration.html', args)


def profile(request, id=None):
    if id is None:
        return HttpResponseRedirect('/account/profile/%d/' % request.user.id)
    user = get_object_or_404(User, id=id)
    user_profile = get_object_or_404(UserProfile, user=user)
    comments = Comment.objects.filter(user_profile=user_profile)
    args = {
        'user': user,
        'current_user': request.user,
        'comments': comments
    }
    if request.method == 'POST':
        commentForm = AddCommentForm(request.POST, author=request.user, user_profile=user_profile)
        if commentForm.is_valid():
            commentForm.save()
            return redirect('accounts:profile_with_id', id=id)
        else:
            args['commentForm'] = commentForm
            return render(request, 'accounts/profile.html', args)
    else:
        commentForm = AddCommentForm(author=request.user, user_profile=user_profile)
        args['commentForm'] = commentForm
        return render(request, 'accounts/profile.html', args)


@login_required(login_url="/account/login")
def edit_profile(request):
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST,
                                 instance=request.user
                                 )
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile
                                   )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('/account/profile')
        else:
            args = {
                'p_form': p_form,
                'u_form': u_form,
            }
            return render(request, 'accounts/profile_edit.html', args)
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        args = {
            'p_form': p_form,
            'u_form': u_form,
        }
        return render(request, 'accounts/profile_edit.html', args)


def catalog(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    users = User.objects.all()
    return render(request, 'accounts/users_catalog.html', {
        'users': users,
        'current_user': user
    })


@login_required(login_url="/account/login")
def current_user(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def projects_catalog(request):
    projects = ProjectPage.objects.all()
    user = request.user
    return render(request, 'projects/projects_all.html', {
        'user': user,
        'projects': projects
    })


def project_page(request, id):
    project = get_object_or_404(ProjectPage, id=id)
    comments = Comment.objects.filter(project=project)
    args = {
        'project': project,
        'current_user': request.user,
        'comments': comments
    }
    if request.method == 'POST':
        waitingList = request.POST.get('waitingList', False)
        if waitingList:
            project.waiting_list.remove(waitingList)
            project.participants.add(waitingList)
            project.save()
            return redirect('accounts:project', id=id)

        participantList = request.POST.get('participantList', False)
        if participantList:
            project.participants.remove(participantList)
            project.save()
            return redirect('accounts:project', id=id)

        commentForm = AddCommentForm(request.POST, author=request.user, project=project)
        if commentForm.is_valid():
            commentForm.save()
            return redirect('accounts:project', id=id)
        else:
            args['commentForm'] = commentForm
            return render(request, 'projects/project.html', args)
    else:
        commentForm = AddCommentForm(author=request.user, project=project)
        args['commentForm'] = commentForm
        return render(request, 'projects/project.html', args)


@login_required(login_url="/account/login")
def create_project(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, owner=request.user)
        if form.is_valid():
            form.save()
            return redirect('../projects_catalog')
        else:
            args = {'form': form}
            return render(request, 'projects/create.html', args)
    else:
        form = ProjectCreateForm()
        args = {'form': form}
        return render(request, 'projects/create.html', args)


@login_required(login_url="/account/login")
def edit_project(request, id):
    project = get_object_or_404(ProjectPage, id=id)
    if request.method == 'POST':
        project_form = EditProjectForm(request.POST,
                                       request.FILES,
                                       instance=project
                                       )
        if project_form.is_valid():
            project_form.save()
            return HttpResponseRedirect('/account/project/%s/' % id)
        else:
            args = {
                'form': project_form
            }
            return render(request, 'projects/edit.html', args)
    else:
        project_form = EditProjectForm(instance=project)
        args = {
            'form': project_form,
            'project': project,
        }
        return render(request, 'projects/edit.html', args)


@login_required(login_url="/account/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


@login_required(login_url="/account/login")
def delete_project(request, id):
    project = get_object_or_404(ProjectPage, id=id)
    project.delete()
    return HttpResponseRedirect('/account/projects_catalog/')


def search_form(request):
    return render(request, 'projects/test.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        filter = ProjectPage.objects.filter(Q(description__contains=q) | Q(type__contains=q) | Q(title__contains=q))
        args = {'filter': filter, 'query': q}
        print(len(filter))
        return render(request, 'projects/results.html', args)
    else:
        return HttpResponse('Please submit a search term.')


def applying_to_project(request, id=None):
    project = get_object_or_404(ProjectPage, id=id)
    project.waiting_list.add(request.user.id)
    project.save()
    return redirect('accounts:project', id=id)


def delete_from_waitinglist(request, id=None):
    project = get_object_or_404(ProjectPage, id=id)
    project.waiting_list.remove(request.user.id)
    project.save()
    return redirect('accounts:project', id=id)
