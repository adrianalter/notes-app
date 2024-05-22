from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Specify the fields to include in the serialized representation
        fields = ["id", "username", "password"]
        # Set the password field as write-only, means that the password will be included in the serialized representation when creating or updating a user, but it will not be included when retrieving user data.
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        # Create a new user instance using the validated data
        user = User.objects.create_user(**validated_data)
        # Return the newly created user instance
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","title","content","created_at","author"]
        extra_kwargs = {"author": {"read_only": True}}