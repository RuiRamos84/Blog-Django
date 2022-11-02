from django.urls import path
from . views import  UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilPageView, EditProfilePageView, CreateprofilePageView
from . import views





urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name= 'registration/change_password.html'), name='change_password'),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilPageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateprofilePageView.as_view(), name='create_profile_page'),
] 


