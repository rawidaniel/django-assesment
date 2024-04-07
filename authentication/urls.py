from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

# app_name = "core"


urlpatterns = [
    path('signup/', UserViewSet.as_view({'post': 'create'}), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("activation/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "activate"}), name="activate"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("reset-password-confirm/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
]
