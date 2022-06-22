from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 
import blogs 


app_name = 'account'

urlpatterns = [
    #Post views
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),

    #Password change after logging in
    path('password_change/', auth_views.PasswordChangeView.as_view(),
     name="password_change"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
     name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(),
     name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
     name='password_reset_complete'),
    
    #Registration urls
    path('register/', views.register, name='register'),
    
    #Edit profile urls 
    path('edit/', views.edit, name='edit' ),

    # path to blogs application 
    #path('blogs/', blogs:views.post_list, name='post_list'),

]
