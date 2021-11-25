from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView

from userauth.forms import UserInfoCreateForm
from userauth.models import UserInfo


class UserDetail(DetailView):
    model = User
    queryset = User.objects.select_related('userinfo').only('userinfo__about', 'username', 'first_name', 'last_name',
                                                            'email', 'userinfo__user_pic')
    slug_url_kwarg = 'username'
    slug_field = 'username'
    context_object_name = 'user_object'


class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('main-page')
    form_class = UserCreationForm


class UserUpdate(UserPassesTestMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email',)
    slug_url_kwarg = 'username'
    slug_field = 'username'

    def get_success_url(self):
        return reverse('user-detail', kwargs={'username': self.kwargs['username']})

    def test_func(self):
        return self.request.user.username == self.kwargs['username'] \
               or self.request.user.has_perm('authuser.change_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs['username']
        return context


class UserInfoUpdate(UserPassesTestMixin, UpdateView):
    model = UserInfo
    fields = ('about', 'user_pic',)

    def get_success_url(self):
        return reverse('user-detail', kwargs={'username': self.kwargs['slug']})

    def test_func(self):
        return self.request.user.username == self.kwargs['slug'] \
               or self.request.user.has_perm('userauth.change_userinfo')


class UserInfoCreate(UserPassesTestMixin, CreateView):
    model = UserInfo
    form_class = UserInfoCreateForm

    def get_success_url(self):
        return reverse('user-detail', kwargs={'username': self.kwargs['slug']})

    def form_valid(self, form):
        form.instance.author_user = self.request.user
        form.instance.user = get_object_or_404(User, username=self.kwargs['username'])
        form.instance.slug = self.kwargs['username']
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == self.kwargs['username'] \
               or self.request.user.has_perm('userauth.change_userinfo')
