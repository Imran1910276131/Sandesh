from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets,views
from .models import Profile
from django.http import JsonResponse
from .serializers import ProfileSerializer,UserSerializer
from django.views import View
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .tasks import scrape_news
User=get_user_model()

class Scrapper(View):
    def get(self, request):
        scrape_news.delay()
        return JsonResponse({'message': 'All News scrapping has been scheduled.'}, status=200)
        


        


# class WorldViewData(viewsets.ModelViewSet):
#     queryset=World.objects.all().order_by("-id")
#     serializer_class=WorldSerializer


# class SportViewData(viewsets.ModelViewSet):
#     queryset=Sports.objects.all().order_by("-id")
#     serializer_class=SportsSerializer

# class TradeViewData(viewsets.ModelViewSet):
#     queryset=Trade.objects.all().order_by("-id")
#     serializer_class=TradeSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        user = request.user
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response({"message": "Request is Get", "userdata": serializer.data})

    def post(self, request):
        user = request.user
        profile = Profile.objects.get(user=user)
        data = request.data

        # Handle profile image upload
        if 'profile_image' in data:
            profile.image = data['profile_image']
            profile.save()
            return Response({"message": "Image uploaded successfully", "image_url": profile.image.url})

        # Handle profile data update
        user_data = {
            'first_name': data.get('first_name', user.first_name),
            'last_name': data.get('last_name', user.last_name),
            'email': data.get('email', user.email)
        }

        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
        else:
            return Response({"message": "Profile update failed", "errors": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileSerializer(profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully", "userdata": serializer.data})
        return Response({"message": "Profile update failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class RegisterView(views.APIView):
    def post(self,request):
        serializers=UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            user=User.objects.get(username=serializers.data['username'])
            token_obj,_=Token.objects.get_or_create(user=user)
            return Response({"error":False,"message":"User creation Successfull","data":serializers.data,"token":str(token_obj)})
        return Response({"error":True,"message":"A user with that name already exists! Try another username","data":serializers.data})

