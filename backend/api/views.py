from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status, permissions
from .serializers import UserSerializer, UserSerializerList, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # return Note.objects.all()
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    # queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# class UserList(APIView):
#     def get(self, request, format=None):
#         # Get the title from the query parameters (if none, default to empty string)
#         username = request.query_params.get("username", "")

#         if username:
#             # Filter the queryset based on the title
#             user_posts = User.objects.filter(username__icontains=username)
#         else:
#             # If no title is provided, return all blog posts
#             user_posts = User.objects.all()

#         serializer = UserSerializer(user_posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     # authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAdminUser]
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)

# class ListUsers(generics.ListCreateAPIView):
class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]