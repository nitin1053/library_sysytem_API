from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    RegisterView,
    SignInView,
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<str:isbn>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
