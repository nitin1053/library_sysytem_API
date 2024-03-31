from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'publication_date', 'isbn', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username']  # Changed 'user_name' to 'username'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        
        return user

