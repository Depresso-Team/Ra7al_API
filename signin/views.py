# Import necessary modules from Django REST framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

# Import models and serializers from application
from .models import User, Guide
from .serializers import UserSerializer, GuideSerializer , UserLoginSerializer , GuideLoginSerializer



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
            password = serializer.validated_data['password']
            
            try:
                user = User.objects.get(email_address=email)
            except User.DoesNotExist:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
            if check_password(password, user.password):
                # Return user data in the response
                user_serializer = UserSerializer(user)  # Replace with your user serializer
                return Response({'detail': 'Login successful', 'user': user_serializer.data})
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GuideLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GuideLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email_address']
            password = serializer.validated_data['password']
            
            try:
                guide = Guide.objects.get(email_address=email)
            except Guide.DoesNotExist:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
            if check_password(password, guide.password):
                # Return guide data in the response
                guide_serializer = GuideSerializer(guide)  # Replace with your guide serializer
                return Response({'detail': 'Login successful', 'guide': guide_serializer.data})
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)