from django.urls import path
from rest_auth.views import LogoutView
from . import views

app_name = 'account'
urlpatterns = [

    path('validate_phone/', views.ValidatePhoneSendOTP.as_view(), name='validate_phone'),
    path('validate_otp/', views.ValidateOTP.as_view(), name='validate_otp'),
    path('registration/', views.Register.as_view(), name='registration'),
    path('forget_password/', views.ValidatePhoneForgotPassword.as_view(), name='forget_password'),
    path('forget_password_otp/', views.ValidateOTPForgetPassword.as_view(), name='forget_password_otp'),
    path('forget_password_change/', views.ForgetPasswordChange.as_view(), name='forget_password_change'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', views.UserRetrieveUpdateView.as_view(), name='dashboard'),

]

