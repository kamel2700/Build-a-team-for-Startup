from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^profile/logout/$', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^profile/change_password$', views.change_password, name='password_change'),

    url(r'^reset_password/$', PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
        name='password_reset'),
    url(r'^reset_password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset_password/complete/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<id>\d+)/$', views.profile, name='profile_with_id'),

    url(r'^profile/edit$', views.edit_profile, name='profile_edit'),
    url(r'^catalog/$', views.catalog, name='profiles_catalog'),

    url(r'^projects_catalog/?$', views.projects_catalog, name='projects_catalog'),
    url(r'^project/(?P<id>\d+)/$', views.project_page, name='project'),

    url(r'^projects/create$', views.create_project, name='project_create'),
    url(r'^project/(?P<id>\d+)/edit$', views.edit_project, name='project_edit'),
    url(r'^project/(?P<id>\d+)/delete', views.delete_project, name='project_delete'),
    url(r'^project/(?P<id>\d+)/applytoproject', views.applying_to_project, name='project_applying'),
    url(r'^project/(?P<id>\d+)/removefromlist', views.delete_from_waitinglist, name='removefromparticipate'),

    url(r'^search/$', views.search, name='search')
]
