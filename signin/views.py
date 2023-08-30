# Import necessary modules from Django REST framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User

# Import models and serializers from application
from .models import User, Guide
from .serializers import UserSerializer, GuideSerializer , UserLoginSerializer



# User registration view using APIView
class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Your logic for creating a new user
        class UserRegistrationView(viewsets.ModelViewSet):
              queryset = User.objects.all()
              serializer_class = UserSerializer

        # Assuming 'user' is the created user object
        message = User.session_message
        return Response({"message": message}, status=status.HTTP_201_CREATED)


# Guide registration view using APIView
class GuideCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Your logic for creating a new guide
        class GuideRegistrationView(viewsets.ModelViewSet):
              queryset = Guide.objects.all()
              serializer_class = GuideSerializer

        # Assuming 'guide' is the created guide object
        message = Guide.session_message
        return Response({"message": message}, status=status.HTTP_201_CREATED)




# User registration viewset
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Guide registration viewset
class GuideRegistrationView(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email_address']
            phone_number = serializer.validated_data['phone_number']

            try:
                user = User.objects.get(email_address=email, phone_number=phone_number)
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)