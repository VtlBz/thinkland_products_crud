# /api/v1/users/

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.v1.users.views import UserRegistrationView

urlpatterns = [
    path('register/',
         UserRegistrationView.as_view(),
         name='user_registration'),
    path('token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh')
]
