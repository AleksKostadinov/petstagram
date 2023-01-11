from django.urls import include, path

from petstagram.accounts.views import SignInView, SignOutView, SignUpView, UserDetailsView, delete_user, edit_user


urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('delete/', delete_user, name='delete user'),
        path('edit/', edit_user, name='edit user'),
    ])),
]
