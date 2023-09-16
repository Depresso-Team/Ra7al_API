from django.shortcuts import render
from rest_framework import status , generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser , Guide , GuidesReviews
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView




# Register a new user
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Create a dynamic error message based on the field errors
            error_message = 'Error: '
            for field, errors in serializer.errors.items():
                error_message += f"{field}: {', '.join(errors)}"

            return Response({'error_message': error_message}, status=status.HTTP_406_NOT_ACCEPTABLE)
    


# Register a new user by CBV (generics)    
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer



# Logout a user
@api_view(['POST'])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Get the username of the logged-out user
            username = request.user.username

            # Delete the user's token to log out
            request.user.auth_token.delete()

            return Response({'message': f'{username} logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        


# Login a user or guide
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')

        user = None

        # Attempt to find the user by email
        try:
            user = CustomUser.objects.get(email=username_or_email)
        except ObjectDoesNotExist:
            pass

        # If not found by email, attempt to find the user by username
        if not user:
            user = CustomUser.objects.filter(username=username_or_email).first()

        if user and user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)  # Pass the user instance to the serializer
            serialized_data = serializer.data
            serialized_data['token'] = token.key  # Add the token data to the serialized user data

            # Check if the user is a guide and include guide-specific data
            if user.is_guide:
                guide = Guide.objects.get(user=user)
                serialized_data['rate'] = guide.rate
                serialized_data['reviews'] = guide.reviews
                serialized_data['personal_photo'] = guide.personal_photo
                serialized_data['is_approved'] = guide.is_approved

            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


    



# Get all users
@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


# Retrive , Update , Delete a user or guide
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer





# Guides List
# class GuideList(APIView):
#     def get(self, request, format=None):
#         guides = Guide.objects.all()
#         serializer = GuideSerializer(guides, many=True)

#         response_data = {
#             "status": True,
#             "message": "success",
#             "guides": serializer.data
#         }

#         return Response(response_data)






class GuideListView(ListAPIView):
    queryset = Guide.objects.all()  # You can customize the queryset as needed
    serializer_class = GuideListSerializer





# Best Guides , filtered by rate
class HighestRatedGuide(APIView):
    def get(self, request):
        # Get all guides that are approved, ordered by rate in descending order
        guides = Guide.objects.filter(is_approved=True).order_by('-rate')

        # Limit the queryset to the top 5 results
        guides = guides[:5]

        # Serialize the guides using the HighestRatedGuideSerializer
        serializer = HighestRatedGuideSerializer(guides, many=True)
        
        response_data = {
            "status": True,
            "message": "success",
            "guides": serializer.data
        }

        return Response(response_data)






# Save a Guide
class SaveGuideView(APIView):
    def post(self, request):
        serializer = SaveGuideSerializer(data=request.data)
        if serializer.is_valid():
            guide_id = serializer.validated_data['guide_id']
            try:
                guide = Guide.objects.get(pk=guide_id)
                guide.saved = True
                guide.save()
                return Response({'message': 'Guide saved successfully.'})
            except Guide.DoesNotExist:
                return Response({'message': 'Guide not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Saved Guides List
class SavedGuidesListView(ListAPIView):
    queryset = Guide.objects.filter(saved=True)  # Filter saved guides
    serializer_class = SavedGuidesSerializer




# Guide Detail
class GuideDetailView(generics.RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer



