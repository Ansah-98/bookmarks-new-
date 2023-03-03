from django.urls import path
from .views import login_view,dashboard,registration,profile_register,user_list,user_detail,user_follow
from django.contrib.auth import views as auth_views


urlpatterns = [#path('login/',login_view, name = 'login'),
        path('login/',auth_views.LoginView.as_view(), name='sign-in'),             path('logout', auth_views.LogoutView.as_view(), name = 'logout'),
        path('dashboard', dashboard , name= 'dashboard'),
        path('password_change/', auth_views.PasswordChangeView.as_view(), name = 'password-change'),
        path('password_change_done', auth_views.PasswordChangeDoneView.as_view(), name = 'p_change_done'),
        path('password_reset', auth_views.PasswordResetView.as_view(), name = 'password-reset'),
        path('password-reset-done',auth_views.PasswordResetDoneView.as_view(), name = 'password-reset-done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'reset-confirm'),
        path('reset-done',auth_views.PasswordResetCompleteView.as_view(),name = 'reset-complete'),
        path('register_user', registration,name  = 'user-registration' ),
        path('pro_register', profile_register,name = 'profile-register' ),
        path('users', user_list,name='user-list' ),
        path('user-detail/username', user_detail, name  = 'user_detail'),
        path('follow',user_follow,name = 'follow')]
