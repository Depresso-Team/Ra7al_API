from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Your logic for creating a new user
        class UserRegistrationView(viewsets.ModelViewSet):
              queryset = User.objects.all()
              serializer_class = UserSerializer

        # Assuming 'user' is the created user object
        message = User.session_message
        return Response({"message": message}, status=status.HTTP_201_CREATED)






class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
