from rest_framework import viewsets
from .models import User, Guide
from .serializers import UserSerializer , GuideSerializer
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



class GuideCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Your logic for creating a new guide
        class GuideRegistrationView(viewsets.ModelViewSet):
              queryset = Guide.objects.all()
              serializer_class = GuideSerializer

        # Assuming 'guide' is the created guide object
        message = Guide.session_message
        return Response({"message": message}, status=status.HTTP_201_CREATED)



# ================================================================================================

class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class GuideRegistrationView(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer