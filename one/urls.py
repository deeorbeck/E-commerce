from django.urls import path
from .views import *
from django.contrib.auth import views as authviews

urlpatterns = [
    path('', customer, name = 'customer'),
    path('product/<int:pk>/' , productView, name = 'view'),
    path('basket/' , basket , name='basket'),
    path('login/', loginPage , name = 'login'),
    path('signup/', signupPage , name = 'signup'),
    path('logout/', logoutPage , name = 'logout'),
#

    path('reset_password/',
             authviews.PasswordResetView.as_view(template_name = 'reset_password/reset_password.html'),
             name = 'reset_password'
         ),
    path('reset_password_sent/',
         authviews.PasswordResetDoneView.as_view(template_name = 'reset_password/sentpage.html'),
         name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',
         authviews.PasswordResetConfirmView.as_view(template_name = 'reset_password/confirm.html'),
         name = 'password_reset_confirm'),
    path('reset_password_complete/',
         authviews.PasswordResetCompleteView.as_view(template_name = 'reset_password/complete.html'),
         name = 'password_reset_complete'),
    path('pay/',tolov, name='pay'),
]