from django.contrib.auth.views import LoginView
from django.urls import path


from .views import (
    get_cookie_view,
    set_cookie_view,
    set_sessions_view,
    get_sessions_view,
    MyLogoutView,
    AboutMeView,
    RegisterView,
    FooBarView,
    ProfilePictureView,
    UserListView,
    UserDetailView,
    AvatarUpdateView,
)

app_name = "myauth"

urlpatterns = [
    path("login/",
         LoginView.as_view(
             template_name="myauth/login.html",
             redirect_authenticated_user=True,
         ),
         name="login",
         ),

    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path('users-list/', UserListView.as_view(), name='users_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('change-avatar/', ProfilePictureView.as_view(), name='change_avatar'),
    path('<int:user_id>/update-avatar/', AvatarUpdateView.as_view(), name='update_avatar'),
    path("register/", RegisterView.as_view(), name="register"),
    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),
    path("session/set/", set_sessions_view, name="session-set"),
    path("session/get/", get_sessions_view, name="session-get"),
    path("foo-bar/", FooBarView.as_view(), name="foo-bar")
]
