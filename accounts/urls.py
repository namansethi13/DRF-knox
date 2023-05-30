from knox import views as knox_views
from .views import RegisterAPI ,ChangePasswordView
from django.urls import path

from .views import LoginAPI , RegisterAPI , getuser
from .verifymail import verify_mail
urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('login', LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('user', getuser, name='getuser'), #this is just for testing the authentication
    path('verify_token/<slug:verify_token>',verify_mail)

]