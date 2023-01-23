from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from petstagram.accounts.forms import UserCreateForm

# Always get the 'user model' with 'get_user_model'
UserModel = get_user_model()

# def login_user(request):
#     return render(request, 'accounts/login-page.html')


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


# def register_user(request):
#     return render(request, 'accounts/register-page.html')


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        login(request, self.object)
        
        return response
        


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')

# N+1 QueryProblem

class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        # context['photos_count'] = self.request.user
        context['pets_count'] = self.object.pet_set.count()
        
        photos = self.object.photo_set.prefetch_related('photolike_set')
        
        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context

# def details_user(request, pk):
#     return render(request, 'accounts/profile-details-page.html')


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
    
    
# def delete_user(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })

# def edit_user(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')
