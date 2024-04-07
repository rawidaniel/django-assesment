from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

# app_name = "core"


urlpatterns = [
    path('signup/', UserViewSet.as_view({'post': 'create'}), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("reset-password-confirm/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
]
