from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Book
from .serializers import BookSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class SignInView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        username=request.data.get('username')
        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 'success',
                'user_id': user.id,
                'username':username,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        else:
            return Response({'status': 'failed', 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'isbn'
