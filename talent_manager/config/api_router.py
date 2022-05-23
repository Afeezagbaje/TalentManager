from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from talent_manager.users.api.views.users import UserViewSet
from talent_manager.users.api.views.register import RegisterView
from talent_manager.users.api.views.login import LoginView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
]

app_name = "api"
urlpatterns += router.urls
