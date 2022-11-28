from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

# Create your views here.
class Login(APIView):
    def post(self,request) -> Response:
        # Get data
        email = request.data.get('email')
        password = request.data.get('password')
        # Get user
        try:
            user = User.objects.get(email = email)
            if user.check_password(password):
                token = RefreshToken.for_user(user=user)
                serializer = UserSerializer(user)
                data = {
                    'user': serializer.data,
                    'refresh': str(token),
                    'access': str(token.access_token)
                }
                return Response(data,status=status.HTTP_200_OK) 
        except User.DoesNotExist:
            pass
        return Response({'message': 'Invalid username and/or password.','status': 404},status=status.HTTP_401_UNAUTHORIZED)



class Register(APIView):
    
    def post(self,request) -> Response:
        return Response({'message':'God is Good Forever'},status=status.HTTP_200_OK)