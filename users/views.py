import jwt
from datetime import *
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView



class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class TodosListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TodosRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User Not Found')
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        
        payload = {
            'id':user.id,
            'exp': str(datetime.now()) + str(timedelta(minutes=60)),
            'iat':  str(datetime.now())
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        
        response = Response()
        response.set_cookie(key='jwt', value=token,   httponly=True)
        response.data = {
            'jwt': token
        }
        return response