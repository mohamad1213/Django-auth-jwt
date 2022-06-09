from django.urls import path
# from .views import RegisterView, LoginView, AuthView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import UserCreate, TodosListCreateView, TodosRetrieveUpdateDestroyAPIView
from .views import LoginView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Authenticated API')

urlpatterns = [
    path("", schema_view),
    # path('', TodosListCreateView.as_view()),
    # path('login', LoginView.as_view()),
    path("registration/", UserCreate.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
