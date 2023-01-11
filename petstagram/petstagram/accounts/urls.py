from django.urls import include, path

from petstagram.accounts.views import SignInView, SignUpView, delete_user, details_user, edit_user


urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('delete/', delete_user, name='delete user'),
        path('edit/', edit_user, name='edit user'),
    ])),
]
