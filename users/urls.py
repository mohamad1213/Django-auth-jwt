from django.urls import path
# from .views import RegisterView, LoginView, AuthView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import UserCreate, TodosListCreateView, TodosRetrieveUpdateDestroyAPIView
from .views import LoginView


urlpatterns = [
    path("registration/", UserCreate.as_view()),
    # path('', TodosListCreateView.as_view()),
    # path('login', LoginView.as_view()),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
