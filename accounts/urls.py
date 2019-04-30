from django.urls import path, include	
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
	# path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html', success_url='/accounts/password_change_done'), name='password_change'),
	path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',success_url='/accounts/password_reset_done'), name='password_reset'),
	path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', success_url='/accounts/reset_done/'), name='password_reset_confirm'),
	path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
	# path('', include('django.contrib.auth.urls')),
	path('register/', views.register, name='register'),
	path('edit/', views.edit, name='edit'),
	path('', views.dashboard, name='dashboard'),


	path('users/', views.user_list, name='user_list'),
	path('users/<username>', views.user_detail, name='user_detail'),
	path('users/follow/', views.user_follow, name='user_follow'),
]