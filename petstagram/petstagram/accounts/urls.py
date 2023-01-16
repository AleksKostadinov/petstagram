from django.urls import include, path

from petstagram.accounts.views import UserDeleteView, UserEditView, SignInView, SignOutView, SignUpView, UserDetailsView


urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
    ])),
]
