from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from users.views import *

urlpatterns = [
    path('signup/', SignupView.as_view()),
    # path('login/', LoginView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('<int:user_id>/', UserInfoView.as_view()),
    path('waitings/', UserWaitingView.as_view()),
]
