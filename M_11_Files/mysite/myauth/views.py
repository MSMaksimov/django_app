from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic.edit import FormView, UpdateView


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class ProfilePictureView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'myauth/change_avatar.html'
    form_class = ProfilePictureForm
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user.profile
        return kwargs

    def test_func(self):
        profile = self.get_object()
        return self.request.user.is_authenticated and (self.request.user.is_staff or profile.user == self.request.user)

    def get_object(self, queryset=None):
        return self.request.user.profile


class AvatarUpdateView(UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfilePictureForm
    template_name = 'myauth/avatar_update.html'

    def get_object(self, queryset=None):
        user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return Profile.objects.get_or_create(user=user)[0]

    # def get_object(self, queryset=None):
    #     user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
    #     profile, created = Profile.objects.get_or_create(user=user)
    #     if created:
    #         # profile was just created, redirect to edit profile page
    #         return redirect('myauth:user_update')
    #     return profile

    def get_success_url(self):
        return reverse_lazy('myauth:user_detail', kwargs={'pk': self.kwargs.get('user_id')})

    def test_func(self):
        return self.request.user.is_staff or self.request.user.pk == int(self.kwargs.get('user_id'))

    # def get_context_data(self, **kwargs):
    #     print('AvatarUpdateView.get_context_data called')
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = self.get_form()
    #     return context


class UserListView(ListView):
    model = User
    template_name = 'myauth/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset()
        return queryset


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'myauth/user_detail.html'
    context_object_name = 'user'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


@user_passes_test(lambda u: u.is_superuser)
def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_sessions_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_sessions_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})
