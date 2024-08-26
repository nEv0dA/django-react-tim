from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
        
class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

## Example
# from django.contrib.auth.hashers import make_password

# user = User.objects.create(
#        email=validated_data['email'],
#        username=validated_data['username'],
#        password = make_password(validated_data['password'])
# )
## see also https://stackoverflow.com/questions/69972644/drf-simple-jwt-no-active-account-found-with-the-given-credentials