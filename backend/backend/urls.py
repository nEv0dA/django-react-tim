from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, ListUsers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/user/", UserList.as_view(), name="user"),
    path("api/user/", ListUsers.as_view(), name="user"),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]
